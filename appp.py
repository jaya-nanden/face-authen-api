from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from PIL import Image

import os
import os.path
import numpy

import json
import base64
import io

import face_recognition
import cv2

from spreadsheet_update import append_data, read_data

# os.chdir('../images')
known_encodings = []
known_names = []
# print(os.listdir(known_dir))

def create_embedding(roll_no):
    try:
        known_dir = './known/'+str(roll_no)

        def read_img(path):
            img = cv2.imread(path)
            (h,w) = img.shape[:2]
            width = 500
            ratio = width/float(w)
            height = int(h*ratio)
            return cv2.resize(img,(width,height))


        for file in os.listdir(known_dir):
            img = read_img(known_dir +'/'+ file)
            img_enc = face_recognition.face_encodings(img)[0]
            known_encodings.append(img_enc)
            known_names.append(file.split('.')[0])

        return known_encodings,known_names
    except:
        return 0,0


# Take in base64 string and return image
def stringToRGB(s):
    b64string = str(s)
    # b64string += '=' * (-len(s) % 4)
    imgdata = base64.b64decode(b64string)
    image = Image.open(io.BytesIO(imgdata))
    # print(image.width)
    return image


# Initializing flask application
app = Flask(__name__,  template_folder='template')
cors = CORS(app)


@app.route("/create", methods=["GET", "POST"])
def index():
    return render_template('create.html')

@app.route("/read", methods=["GET", "POST"])
def read():
    emotion_dict = {"Angry": 0, "Disgusted": 0, "Fearful": 0, "Happy": 0, "Neutral": 0 , "Sad": 0,  "Surprised": 0, "IDK": 0}

    df = read_data()
    count_dict = df['emotion'].value_counts().to_dict()
    # print(count_dict)
    for key, value in count_dict.items():
        emotion_dict[key] = value

    # print(emotion_dict)
    response = app.response_class(response=json.dumps(emotion_dict),
                                  status=200,
                                  mimetype='application/json')
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"

    return response

@app.route("/predict", methods=["POST"])
def process_image():
    rawData = request.data
    # print(rawData)
    dictData = json.loads(rawData.decode('utf-8'))
    roll_no = dictData['rollno']
    status = "No"
    emotion = "nil"
    # print(roll_no)
    known_encodings,known_names=create_embedding(roll_no)
    face_detected = 1
    if(known_encodings != 0 and known_names != 0):

        base64 = dictData['imgbase64']
        string64 = base64.split(',')[1]  # Only for base64 from JS
        img = stringToRGB(string64)
        
        I = numpy.array(img)
        I = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)

        if(face_recognition.face_encodings(I) == []):
            # print("no face_detected")
            status = "No Face Captured"
        else:
            img_enc = face_recognition.face_encodings(I)[0]
            results = face_recognition.compare_faces(known_encodings, img_enc)
            dist = face_recognition.face_distance(known_encodings, img_enc)

            name = "nil"
            f=0
            #print(results)
            for i in range(len(results)):
                if(results[i]):
                    f=1
                    name = known_names[i]
                    name=name[:len(name) - 5]
                    min_dist=dist[i]
                    min_dist=round((100 - min_dist),2)
                    min_dist=str(min_dist)
                    # emotion = emotion_recog(I)
                    # print(emotion, name, min_dist)
                    break
            if(f == 0):
                name = "no_match"
                min_dist = -1
            if(roll_no == name):
                status = "Yes"
            else:
                status = "No"
    else:
        status = "error"

    # print(face_detected, status)

    # Appending Data to csv
    if(status == "Yes"):
        append_data([status, emotion])

    # Data in JSON-serializable type
    data = {'rollno': str(roll_no),  'match_status': status} 
    # print(data)
    response = app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json')
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"

    return response


if __name__ == "__main__":
    app.run(debug = True)

import face_recognition
import cv2
import os,sys
import numpy as np
import os


def read_img(path):
  img=cv2.imread(path)
  (h,w)=img.shape[:2]
  width=500
  ratio=width/float(w)
  height=int(h*ratio)
  return cv2.resize(img,(width,height))

known_encodings=[]
known_names=[]
known_dir='./known'

for file in os.listdir(known_dir):
  img=read_img(known_dir +'/'+file)
  img_enc=face_recognition.face_encodings(img)[0]
  known_encodings.append(img_enc)
  known_names.append(file.split('.')[0])
  
unknown_dir='./unknown'
for file in os.listdir(unknown_dir):
  print("Processing",file)
  img=read_img(unknown_dir+'/'+file)
  img_enc=face_recognition.face_encodings(img)[0]
  results=face_recognition.compare_faces(known_encodings,img_enc)
  dist=face_recognition.face_distance(known_encodings, img_enc)
  f=0
  #print(file)

  for i in range(len(results)):
        if results[i]:
            f=1
            name = known_names[i]
            name=name[:len(name)-5]
            min_dist=dist[i]
            min_dist=round((100-min_dist),2)
            min_dist=str(min_dist)
            (top, right, bottom, left) = face_recognition.face_locations(img)[0]
            cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(img, name, (left+2, bottom+20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
            cv2.putText(img, min_dist, (right-2, bottom+20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
            cv2.imshow('output',img)

            cv2.waitKey(0)
            cv2.destroyAllWindows()
            break;

  if(f==0):
    print("Did not match with the dataset")

  
  
  #print(results)
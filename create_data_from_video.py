import cv2
import os,sys
import numpy as np
import os


name = str(input("Enter Roll No: ")).lower()
directory = "known/" + name
parent_dir = "./"
  
# Path
path = os.path.join(parent_dir, directory)

try:  
    os.mkdir(path)
except:
    pass

print("Directory '%s' created" %directory)
os.chdir(path)
cwd = os.getcwd()
print("Current working directory is:", cwd)

# Accessing Video file for respective input
vid_dir = "videos" + "\\" + str(name) + ".mp4"
vid_path =  cwd[:-14] + vid_dir 
# print(vid_path)
cap = cv2.VideoCapture(vid_path)


count = 0
while (count < 5):
    count = count + 1
    ret, frame = cap.read()
    
    if (frame is None) == False:
        (h,w) = frame.shape[:2]
        width = 500
        ratio = width/float(w)
        height = int(h*ratio)
        frame = cv2.resize(frame,(width,height))
        if count < 10:
            cv2.imwrite(name+"0000" + str(count) + '.jpg', frame)
        elif count < 100:
            cv2.imwrite(name+"000" + str(count) + '.jpg', frame)
        elif count < 1000:
            cv2.imwrite(name+"00" + str(count) + '.jpg', frame)
        elif count < 10000:
            cv2.imwrite(name+"0" + str(count) + '.jpg', frame)
    else:
        break
    
print(str(str(count) + " images created for" + name))
cap.release()

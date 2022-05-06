import numpy as np 
import os
import cv2
import face_recognition
from datetime import datetime

path = 'Images'
images = []
Names = []

myList = os.listdir(path)
#print(myList)

for nm in myList:
  curr_img = cv2.imread(f'{path}/{nm}')
  images.append(curr_Img)
  Names.append(os.path.splitext(nm)[0])
  #print(Names)
  

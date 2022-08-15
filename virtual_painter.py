import cv2 
import numpy as np
import time
import os
import HandTrackingModule as htm
from PIL import Image
import matplotlib.pyplot as plt
from keras.models import load_model
from main import predict_image

brushThickness=20

cap=cv2.VideoCapture(0)

w=600
h=600

cap.set(3,w)
cap.set(4,h)
# cap.set(3,640)
# cap.set(4,480)

imgCanvas=np.zeros((h,w,3),np.uint8)
# imgCanvas=np.zeros((480,640,3),np.uint8)
width=100
height=100
dimension=(width,height)

detector=htm.handDetector(detectionCon=0.6)

xp,yp=0,0
m=0


	
while True:
	success,img=cap.read()

	img=cv2.flip(img,1)

	img=detector.findHands(img)
	lmList=detector.findPosition(img,draw=False)

	if len(lmList)!=0:

		#tip of index and middle fingers
		x1,y1=lmList[8][1:]
		x2,y2=lmList[12][1:]

		fingers=detector.fingers_up()
		
		if fingers==[1,0,0,0,0]:

			image=Image.fromarray(imgCanvas)
			image.save("img.jpg")
			img = cv2.imread('E:\minor\handwriteen\img.jpg')
			predict_image(img)

			# print(image)

			# processed = keras_process_image(image)
			# pred_probab, pred_class = keras_predict(model1, processed)
			# print(pred_class, pred_probab)
			# cv2.imwrite(f"{m} canvas_img.jpg",imgCanvas)
			# resized=cv2.resize(imgCanvas,dimension,interpolation=cv2.INTER_AREA)
			# cv2.imwrite(f"{m} Resized_img.jpg",resized)
			imgCanvas=np.zeros((h,w,3),np.uint8)
			m+=1
			break

			# imgCanvas=np.zeros((480,640,3),np.uint8)
		if fingers==[0,1,1,0,0]:
			imgCanvas=np.zeros((h,w,3),np.uint8)



		if fingers==[0,1,0,0,0]:
			# cv2.circle(imgCanvas,(x1,y1),15,(255,0,255),cv2.FILLED)
			if xp==0 and yp==0:
				xp,yp=x1,y1
				
			# cv2.line(imgCanvas,(xp,yp),(x1,y1),(255,0,0),brushThickness)
			cv2.line(imgCanvas,(xp,yp),(x1,y1),(255,255,255),brushThickness)
			xp,yp=x1,y1

		
		

	# img=cv2.addWeighted(img,1,imgCanvas,1,0)
	cv2.imshow("Image",img)
	cv2.imshow("Canvas",imgCanvas)
	cv2.waitKey(1)
import numpy as np
import cv2
import os
cap=cv2.VideoCapture('input.mp4')
try:
	#now we are creating the data directires if it is not
	if not os.path.exists('data'):
		os.makedirs('data')
except OSError:
	print('Error is happening')
currentFrame=0
while(True):
	red, frame=cap.read()
	for i in range(0,50):
		red, frame=cap.read()
	name='./data/frame'+str(currentFrame)+'.jpg'
	print('Creating '+name)
	cv2.imwrite(name,frame)
	currentFrame += 1
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.realease()
cv2.destroyAllWindows()

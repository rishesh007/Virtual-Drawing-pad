import numpy as np
import cv2
import cv2.aruco as aruco

yr=50
yb=50
yg=50
b=255
g=255
r=255
rr = 5
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
rows,cols,_= frame.shape
img = np.zeros((rows,cols,3), np.uint8)
def color_pallete(img,x,y,r2,g2,b2):
	for j in range(255):
		cv2.rectangle(img, (520,50+j) , (600,418+j), (0,255-j,0),-1)
		cv2.rectangle(img, (380,50+j) , (450,418+j), (255-j,0,0),-1)
		cv2.rectangle(img, (280,50+j) , (340,418+j), (0,0,255-j),-1)
		cv2.rectangle(img,(200,50+j) , (220,418+j),(255,255,255),-1)
	if y>=50 and y<=480:
		if x>=280 and x<=340:
			# img = cv2.circle(img,`(int(x),int(y)), 5, (255,255,255), -1)
			# cv2.rectangle(img,(100,int(y)-5),(200,5+int(y)),(0.0,0),-1)
			global yr
			yr = y
			# print(yr)
			r2 = int(255-((y-50)//2));
		if x>=380 and x<=450:
			global yb
			yb = y
			# img = cv2.circle(img,(int(x),int(y)), 5, (255,255,255), -1)
			# cv2.rectangle(img,(320,int(yb)-5),(400,5+int(yb)),(0.0,0),-1)
			b2 = int(255-((y-50)//2))
		if x>=520 and x<=600:
			global yg
			yg = y
			# img = cv2.circle(img,(int(x),int(y)), 5, (255,255,255), -1)
			# cv2.rectangle(img,(520,int(yg)-5),(600,5+int(yg)),(0.0,0),-1)
			g2 = int(255-((y-50)//2))
		if x>=200 and x<=220:
			global rr
			rr = (y)
	# img = cv2.circle(img,(447,63), 5, (255,255,255), -1)
	# print(yr)
	img = cv2.circle(img,(int(x),int(rr)), int(rr//10), (b2,g2,r2),-1)
	cv2.rectangle(img,(280,int(yr)-5),(340,5+int(yr)),(255.255,255),-1)
	cv2.rectangle(img,(380,int(yb)-5),(450,5+int(yb)),(255.255,255),-1)
	cv2.rectangle(img,(520,int(yg)-5),(600,5+int(yg)),(255.255,255),-1)
	# cv2.rectangle(img,(150,int(rr)-5),(220,5+int(rr)),(0,0,0),-1)
	return img,r2,b2,g2,(rr//10)

writing_id =2 
pausing_id = 7
while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	frame = cv2.flip( frame, 1 )
	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
	parameters = aruco.DetectorParameters_create()

	corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
	# cv2.rectangle(frame,corners[0][0],corners[1][1],(0,255,0),3)
	# print(ids)
	if ids is not None and len(ids) == 1 and ids[0][0] == 2:
		x1 = corners[0][0][0][0]
		x2 = corners[0][0][1][0]
		x3 = corners[0][0][2][0]
		x4 = corners[0][0][3][0]
		y1 = corners[0][0][0][1]
		y2 = corners[0][0][1][1]
		y3 = corners[0][0][2][1]
		y4 = corners[0][0][3][1]
		x = ((x1+x2)//2 +(x3+x4)//2)//2
		y = ((y1+y4)//2 + (y2+y3)//2)//2
		# print(corners)
		# print(x)
		# print(y)
		cv2.circle(frame,(int(x),int(y)),int(rr),(0,255,0),-1)
		cv2.circle(img,(int(x),int(y)),int(rr),(b,g,r),-1)
		# print(ids.shape)
	if ids is not None and 7 in ids:
		# cv2.rectangle(frame, (480,50) , (590,418), (0,255,0),-1)
		if ids[0][0] == writing_id:
			i = 0
		elif len(ids):
			i = 0
		else:
			i=1
		x1 = corners[i][0][0][0]
		x2 = corners[i][0][1][0]
		x3 = corners[i][0][2][0]
		x4 = corners[i][0][3][0]
		y1 = corners[i][0][0][1]
		y2 = corners[i][0][1][1]
		y3 = corners[i][0][2][1]
		y4 = corners[i][0][3][1]
		x = ((x1+x2)//2 +(x3+x4)//2)//2
		y = ((y1+y4)//2 + (y2+y3)//2)//2
		frame,r,b,g,rr = color_pallete(frame,x,y,r,g,b)
		# if y>=(cols-40) and y<=(cols-10):
		# 	frame = color_pallete(frame,r,b,y)
	cv2.imshow('frame', frame)
	cv2.imshow('img',img)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	if 0xFF == ord('w'):
		img = np.zeros((rows,cols,3), np.uint8)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


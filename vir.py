import numpy as np
import cv2
import cv2.aruco as aruco

# def color_pallete(img,yr,yb,yg):

# 	img = cv2.circle(img,(447,63), 5, (yb,yg,255), -1)
# 	return image

cv2.namedWindow('dst', cv2.WINDOW_NORMAL)
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

def nothing(x):
	pass	

cv2.createTrackbar('R','dst',0,255,nothing)
cv2.createTrackbar('G','dst',0,255,nothing)
cv2.createTrackbar('B','dst',0,255,nothing)

b=255
g=255
r=255
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
rows,cols,_= frame.shape
img = np.zeros((rows,cols,3), np.uint8)
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

	r = cv2.getTrackbarPos('R','dst')
	g = cv2.getTrackbarPos('G','dst')
	b = cv2.getTrackbarPos('B','dst')



	if ids is not None and len(ids) == 1:
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

		r = cv2.getTrackbarPos('R','dst')
		g = cv2.getTrackbarPos('G','dst')
		b = cv2.getTrackbarPos('B','dst')

		cv2.circle(frame,(int(x),int(y)),5,(0,255,0),-1)
		cv2.circle(img,(int(x),int(y)),5,(b,g,r),-1)
		# print(ids.shape)
	if ids is not None and len(ids) == 2:
		# cv2.rectangle(frame, (480,50) , (590,418), (0,255,0),-1)
		if ids[0][0] == writing_id:
			i = 0
		else:
			i = 1
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

		# if y>=(cols-40) and y<=(cols-10):
		# 	frame = color_pallete(frame,r,b,y)
	dst = cv2.addWeighted(img,0.7,frame,0.3,0)
	cv2.imshow('dst',dst)
	cv2.imshow('frame', frame)
	cv2.imshow('img',img)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	if 0xFF == ord('w'):
		img = np.zeros((rows,cols,3), np.uint8)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


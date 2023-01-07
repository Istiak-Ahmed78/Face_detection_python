
import cv2,sys,time,os
# from pantilthat import *

casPath="haarcascade_frontalface_default.xml"
faceCaseCade=cv2.CascadeClassifier(casPath)

FRAME_W = 400
FRAME_H = 300


CENTER_OF_H= FRAME_H/2
CENTER_OF_W=FRAME_W/2

CLOSE_HIGHT = 150
CLOSE_WEIGHT = 150
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  FRAME_W)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_H)
time.sleep(2)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

# def getCenterOfAxis(v):
#     return  F_F_W/2

count=0

def trackTheClosestFace(faces):
    # Closest width
    cWL=200
    cWR=260
    for (x, y, w, h) in faces:
        if(x<cWL):
            turnRight()
        elif(x>cWR):
            
            turnLeft()
        else:
            perform()
        





def perform():
    print('Start greeting')

def turnLeft():
    print('Turn left')

def turnRight():
    print('Turn right')

def isNotAtSide(x):
    return x<260 and x>200
# Is the person close and not at side of the robot
def isClose(x,w,h):
    return (h>CLOSE_HIGHT and w>CLOSE_WEIGHT) and (isNotAtSide(x))

# Is pressed 'Esc' to close camera
def isAppliedForClose():
    k = cv2.waitKey(30) & 0xff
    return k==27

# Draw circle
def drawR(img,x,y,w,h):
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)


# detect faces
def getFaces(gray):

    faces = faceCaseCade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
    )
    return faces




cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces= getFaces(gray)
    for (x, y, w, h) in faces:
        drawR(img,x,y,w,h)
        print('X-axis')
        print(x)
        print('Y-axis')
        print(y)
        print('Hieght')
        print(h)
        trackTheClosestFace(faces)
        if(isClose(x,w,h)):
            perform()
    cv2.imshow('img', img)
    if(isAppliedForClose()):
        break
cap.release()
# Release the VideoCapture object








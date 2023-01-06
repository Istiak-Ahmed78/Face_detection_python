
import cv2,sys,time,os
# from pantilthat import *

casPath="haarcascade_frontalface_default.xml"
faceCaseCade=cv2.CascadeClassifier(casPath)

FRAME_W = 400
FRAME_H = 300
# To capture video from webcam. 
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  FRAME_W)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_H)
time.sleep(2)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

# def getCenterOfAxis(v):
#     return  F_F_W/2

count=0


def getFetch():

    while True:
    # Read the frame
        f, img = cap.read()

        if not f:
            print('We are not receiving data anymore')
            break
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = faceCaseCade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
        )

        # Draw the rectangle around each face

        #Face Square X axis
        print(len(faces))
        if len(faces) != 0:
            (F_F_X,F_F_Y,F_F_W,F_F_H)=faces[0]
            print('We got a face')
            cv2.rectangle(img, (F_F_X, F_F_Y), (F_F_X+F_F_W, F_F_Y+F_F_H), (255, 0, 0), 2)
            
            # Display
            cv2.imshow('img', img)
                # Stop if escape key is pressed
            k = cv2.waitKey(30) & 0xff
            if k==27:
                break
            # return faces[0]
        else:
            print('No face detected')
            # break
    # #Face square Y axis
    # F_F_Y=faces[0].y
    # #Width
    # F_F_W=faces[0].w
    # #Hieght
    # F_F_H=faces[0].h
# face=getFetch()
# if  face is not None:
#     x_center=getCenterOfAxis(F_F_X)
#     print(x_center)

def getFetch():
    print('Be angry')




        
# Release the VideoCapture object
cap.release()







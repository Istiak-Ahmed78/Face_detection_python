
import cv2, time
from gpiozero import Servo
# import RPi.GPIO as GPIO
# from time import sleep

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(3, GPIO.OUT)
# GPIO.setup(13, GPIO.OUT)
# pwmHand=GPIO.PWM(3, 50)
# pwmHead=GPIO.PWM(3, 50)
# pwmHand.start(0)
# pwmHead.start(0)

# def rotatesHeadAngle(angle):
	# duty = angle / 18 + 2
	# GPIO.output(3, True)
	# pwmHead.ChangeDutyCycle(duty)
	# time.sleep(1)
	# GPIO.output(3, False)
	# pwmHead.ChangeDutyCycle(0)


# def rotatedHandAngle(angle):
	# duty = angle / 18 + 2
	# GPIO.output(3, True)
	# pwmHand.ChangeDutyCycle(duty)
	# time.sleep(1)
	# GPIO.output(3, False)
	# pwmHand.ChangeDutyCycle(0)

# pwmHead.stop()
# pwmHand.stop()
# GPIO.cleanup()

casPath="haarcascade_frontalface_default.xml"
faceCaseCade=cv2.CascadeClassifier(casPath)

SERVO_PIN=25



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
    print('Neutralize head angle')
    print('Pull hand up')
    # rotatesHeadAngle(90)
    # rotatedHandAngle(90)


def turnLeft():
    print('Rotate to left. setting head angle at 0')
    # rotatesHeadAngle(0)

def turnRight():
    print('Rotate to right. setting head angle at 180')
    # rotatesHeadAngle(180)

def isNotAtSide(x):
    return x<260 and x>200
# Is the person close and not at side of the robot
def isClose(x,w,h):
    return (h>CLOSE_HIGHT and w>CLOSE_WEIGHT) and (isNotAtSide(x))

# Is pressed 'Esc' to close camera
def isAppliedForClose():
    k = cv2.waitKey(30) & 0xff
    return k==27

# Draw rectangle
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
    if(not cap.isOpened()):
        print('Camera is not found. Actually not opening.')
        break
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
cv2.destroyAllWindows()
# Release the VideoCapture object








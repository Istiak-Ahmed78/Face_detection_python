import cv2,time

casPath="haarcascade_frontalface_default.xml"
faceCaseCade=cv2.CascadeClassifier(casPath)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  400)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
time.sleep(2)

cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    if(not cap.isOpened()):
        print('Camera is not found. Actually not opening.')
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCaseCade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # To stop detecting if 'Esc' is pressed
    k = cv2.waitKey(30) & 0xff
    if(k==27):
        break
    cv2.imshow('img', img)
cap.release()
cv2.destroyAllWindows()
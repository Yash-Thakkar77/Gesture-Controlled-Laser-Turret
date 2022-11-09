import cv2
import mediapipe as mp
import time
import serial
board = serial.Serial('/dev/ttyUSB0', 9600)
cap = cv2.VideoCapture(0)  #in case you are using an external camera, try replacing 0 with 1

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils
board.write(0)   #recalibrates the servo X to position 0
board.write(0)   #recalibrates the servo Y to position 0

while True:
    success, img = cap.read()
    imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm, in enumerate(handLms.landmark):
                if(id==8):  #detects the position of the tip of the index finger in camera frame
                    h, w, c=img.shape
                    cx, cy=int(lm.x*w), int(lm.y*h) #gets the x and y coordinates of tip of index finger
                    angleX=180-(cx/(800/180)) #the (180-) part can be removed. This part is used as I am using the webcam.
                    int (angleX)
                    int (angleY)
                    angleY=180-(cy/(600/180)) #same as line 28. 
                    angleX = round(angleX, -1) #rounds off the coordinates to nearest 10
                    angleY = round(angleY, -1) #rounding off is necessary because the motors go haywire when exact position is given
                    strangleX=str(angleX) #angle for servo X is converted to string so it can be passed to the arduino
                    strangleY=str(angleY) #angle for servo Y is converted to string so it can be passed to the arduino
                    board.write(strangleX.encode())   #write position x to serial port
                    board.write(strangleY.encode())   #write position y to serial port
                    
                    print(angleX, angleY) #printing out the x and y coordinates/angles
                    
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

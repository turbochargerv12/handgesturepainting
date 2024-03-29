from handTracker import *
import cv2
import numpy as np
import random
import base64
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Define the coordinates of the whiteboard
WHITEBOARD_X, WHITEBOARD_Y = 400, 300

# Initialize the MediaPipe Hands model
hands = mp_hands.Hands(static_image_mode = False, max_num_hands = 1, min_detection_confidence = 0.5)


class ColorRect():
    def __init__(self, x, y, w, h, color, text='', alpha = 0.5):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.text = text
        self.alpha = alpha
        
    
    def drawRect(self, img, text_color = (255,255,255), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 0.8, thickness = 2):
        #draw the box
        alpha = self.alpha
        bg_rec = img[self.y : self.y + self.h, self.x : self.x + self.w]
        white_rect = np.ones(bg_rec.shape, dtype = np.uint8)
        white_rect[:] = self.color
        res = cv2.addWeighted(bg_rec, alpha, white_rect, 1-alpha, 1.0)
        
        # Putting the image back to its position
        img[self.y : self.y + self.h, self.x : self.x + self.w] = res

        #put the letter
        tetx_size = cv2.getTextSize(self.text, fontFace, fontScale, thickness)
        text_pos = (int(self.x + self.w/2 - tetx_size[0][0]/2), int(self.y + self.h/2 + tetx_size[0][1]/2))
        cv2.putText(img, self.text,text_pos , fontFace, fontScale,text_color, thickness)


    def isOver(self,x,y):
        if (self.x + self.w > x > self.x) and (self.y + self.h > y > self.y):
            return True
        return False


#initilize the have detector
detector = HandTracker(detectionCon = 0.8)
detect = HandDetector(maxHands = 1, detectionCon = 0.8)

#initilize the camera 
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
cap.set(cv2.CAP_PROP_FPS, 60)
# creating canvas to draw on it
canvas = np.zeros((720,1280,3), np.uint8)

# define a previous point to be used with drawing a line
px,py = 0,0
#initial brush color
color = (255,0,0)
#####
brushSize = 5
eraserSize = 20
####

########### creating colors ########
# Colors button
colorsBtn = ColorRect(200, 0, 100, 100, (120,255,0), 'Colors')

colors = []
# random color
b = int(random.random()*255) - 1
g = int(random.random()*255)
r = int(random.random()*255)
print(b,g,r)
colors.append(ColorRect(300,0,100,100, (b,g,r)))
# red
colors.append(ColorRect(400,0,100,100, (0,0,255)))
# blue
colors.append(ColorRect(500,0,100,100, (255,0,0)))
# green
colors.append(ColorRect(600,0,100,100, (0,255,0)))
# yellow
colors.append(ColorRect(700,0,100,100, (0,255,255)))
# erase (black)
colors.append(ColorRect(800,0,100,100, (0,0,0), "Eraser"))
# clear
clear = ColorRect(900,0,100,100, (100,100,100), "Clear")

########## pen sizes #######
pens = []
for i, penSize in enumerate(range(5,25,5)):
    pens.append(ColorRect(1100,50+100*i,100,100, (50,50,50), str(penSize)))

penBtn = ColorRect(1100, 0, 100, 50, color, 'Pen')

# white board button
boardBtn = ColorRect(50, 0, 100, 100, (255,255,0), 'Board')

#define a white board to draw on
whiteBoard = ColorRect(50, 120, 1020, 580, (255,255,255),alpha = 0.6)

coolingCounter = 20
hideBoard = True
hideColors = True
hidePenSizes = True

while True:
    # Read frame from the webcam
    ret, frame = cap.read()
   
    # Convert the frame to RGB and process it with MediaPipe Hands
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    # If a hand is detected, get the location of the index finger and draw a circle around it
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            index_finger_landmark = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            index_finger_x, index_finger_y = int(index_finger_landmark.x * frame.shape[1]), int(index_finger_landmark.y * frame.shape[0])
            cv2.circle(frame, (index_finger_x, index_finger_y), 10, (0, 255, 0), -1)

            # Calculate the location of the index finger relative to the whiteboard
            whiteboard_index_finger_x, whiteboard_index_finger_y = WHITEBOARD_X + (index_finger_x - frame.shape[1] // 2), WHITEBOARD_Y + (index_finger_y - frame.shape[0] // 2)
            print(f"Index finger location: ({whiteboard_index_finger_x}, {whiteboard_index_finger_y})")

    # Display the resulting frame
    #cv2.imshow('MediaPipe Hands', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    if coolingCounter:
        coolingCounter -=1
        #print(coolingCounter)

    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (1280, 720))
    frame = cv2.flip(frame, 1)
    hnd = detector.findHands(frame, draw=False)
    # try:
    #     if hnd:  
    #         lmlist = hnd[0]
    #         if lmlist:
    #             fingerup = detector.fingersUp(lmlist)
    #             if fingerup == [0, 1, 0, 0, 0]:
                    # if fingerup == [0, 1, 1, 0, 0]:
                        
                    # if fingerup == [0, 1, 1, 1, 0]:
                    #     print('hi')
                    #     clear.alpha = 0 
                    #     canvas = np.zeros((720,1280,3), np.uint8)
                    # if fingerup == [0, 1, 1, 1, 1]:
                    
                    # if fingerup == [1, 1, 1, 1, 1]:
                    
                    # if fingerup == [0, 0, 0, 0, 1]:
    # except Exception:
    #             print('Divided by zero')
    detector.findHands(frame)
    positions = detector.getPostion(frame, draw=False)
    upFingers = detector.getUpFingers(frame)
    print('upFinger = ',upFingers)
    if upFingers:
        x, y = positions[8][0], positions[8][1]
        if upFingers[1] and not whiteBoard.isOver(x, y):
            px, py = 0, 0

            ##### pen sizes ######
            if not hidePenSizes:
                for pen in pens:
                    if pen.isOver(x, y):
                        brushSize = int(pen.text)
                        pen.alpha = 0
                    else:
                        pen.alpha = 0.5

            ####### chose a color for drawing #######
            if not hideColors:
                for cb in colors:
                    if cb.isOver(x, y):
                        color = cb.color
                        cb.alpha = 0
                    else:
                        cb.alpha = 0.5

                #Clear 
                if clear.isOver(x, y):
                    clear.alpha = 0
                    canvas = np.zeros((720,1280,3), np.uint8)
                else:
                    clear.alpha = 0.5
            
            # color button
            if colorsBtn.isOver(x, y) and not coolingCounter:
                coolingCounter = 10
                colorsBtn.alpha = 0
                hideColors = False if hideColors else True
                colorsBtn.text = 'Colors' if hideColors else 'Hide'
            else:
                colorsBtn.alpha = 0.5
            
            # Pen size button
            if penBtn.isOver(x, y) and not coolingCounter:
                coolingCounter = 10
                penBtn.alpha = 0
                hidePenSizes = False if hidePenSizes else True
                penBtn.text = 'Pen' if hidePenSizes else 'Hide'
            else:
                penBtn.alpha = 0.5

            
            #white board button
            if boardBtn.isOver(x, y) and not coolingCounter:
                coolingCounter = 10
                boardBtn.alpha = 0
                hideBoard = False if hideBoard else True
                boardBtn.text = 'Board' if hideBoard else 'Hide'

            else:
                boardBtn.alpha = 0.5

        elif upFingers[1] and not upFingers[2]and not upFingers[3] and not upFingers[4] and not upFingers[0]:
            if whiteBoard.isOver(x, y) and not hideBoard:
                #print('index finger is up')
                cv2.circle(frame, positions[8], brushSize, color,-1)
                #drawing on the canvas
                if px == 0 and py == 0:
                    px, py = positions[8]
                if color == (0,0,0):
                    cv2.line(canvas, (px,py), positions[8], color, eraserSize)
                else:
                    cv2.line(canvas, (px,py), positions[8], color, brushSize)
                px, py = positions[8]
        
        
        elif upFingers == [True,True,False,False,False]:
            clear.alpha = 0 
            canvas = np.zeros((720,1280,3), np.uint8)

        elif upFingers == [False,True,False,False,True]:
            coolingCounter = 10
            boardBtn.alpha = 0
            hideBoard = False
            # hideBoard = False if hideBoard else True
            # boardBtn.text = 'Board' if hideBoard else 'Hide'

        else:
            px, py = 0, 0
    # gesture shown
   

    # put colors button
    colorsBtn.drawRect(frame)
    cv2.rectangle(frame, (colorsBtn.x, colorsBtn.y), (colorsBtn.x +colorsBtn.w, colorsBtn.y+colorsBtn.h), (255,255,255), 2)

    # put white board buttin
    boardBtn.drawRect(frame)
    cv2.rectangle(frame, (boardBtn.x, boardBtn.y), (boardBtn.x +boardBtn.w, boardBtn.y+boardBtn.h), (255,255,255), 2)

    #put the white board on the frame
    if not hideBoard:       
        whiteBoard.drawRect(frame)
        ########### moving the draw to the main image #########
        canvasGray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
        _, imgInv = cv2.threshold(canvasGray, 20, 255, cv2.THRESH_BINARY_INV)
        imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
        frame = cv2.bitwise_and(frame, imgInv)
        frame = cv2.bitwise_or(frame, canvas)


    ########## pen colors' boxes #########
    if not hideColors:
        for c in colors:
            c.drawRect(frame)
            cv2.rectangle(frame, (c.x, c.y), (c.x +c.w, c.y+c.h), (255,255,255), 2)

        clear.drawRect(frame)
        cv2.rectangle(frame, (clear.x, clear.y), (clear.x +clear.w, clear.y+clear.h), (255,255,255), 2)


    ########## brush size boxes ######
    penBtn.color = color
    penBtn.drawRect(frame)
    cv2.rectangle(frame, (penBtn.x, penBtn.y), (penBtn.x +penBtn.w, penBtn.y+penBtn.h), (255,255,255), 2)
    if not hidePenSizes:
        for pen in pens:
            pen.drawRect(frame)
            cv2.rectangle(frame, (pen.x, pen.y), (pen.x +pen.w, pen.y+pen.h), (255,255,255), 2)


    cv2.imshow('video', frame)
    #cv2.imshow('canvas', canvas)
    k= cv2.waitKey(1)
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

import cv2
from cvzone.HandTrackingModule import HandDetector
  
detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(0)
  
while True:
    _, img = video.read()
    img = cv2.flip(img, 1)
    hand = detector.findHands(img, draw=False)
    fing = cv2.imread("C:\\Users\\turbo\\Pictures\\download.png")
    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            if fingerup == [0, 1, 0, 0, 0]:
                fing = cv2.imread("C:\\Users\\turbo\\Pictures\\1.jpg")
            if fingerup == [0, 1, 1, 0, 0]:
                fing = cv2.imread("C:\\Users\\turbo\\Pictures\\2.jpg")
            if fingerup == [0, 1, 1, 1, 0]:
                fing = cv2.imread("C:\\Users\\turbo\\Pictures\\3.jpg")
            if fingerup == [0, 1, 1, 1, 1]:
                fing = cv2.imread("C:\\Users\\turbo\\Pictures\\4.jfif")
            if fingerup == [1, 1, 1, 1, 1]:
                fing = cv2.imread("C:\\Users\\turbo\\Pictures\\5.jfif")
    
    
    
    fing = cv2.resize(fing, (220, 280))
    img[50:330, 20:240] = fing
    cv2.imshow("Video", img)
      
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
          
video.release()
cv2.destroyAllWindows()
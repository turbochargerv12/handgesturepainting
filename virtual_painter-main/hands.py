import cv2
from cvzone.HandTrackingModule import HandDetector
  
detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(0)
  
while True:
    _, img = video.read()
    img = cv2.flip(img, 1)
    hand = detector.findHands(img, draw=False)
    fing = cv2.imread(r"C:\Users\turbo\Documents\GitHub\handgesturepainting\0.jpg")
    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            if fingerup == [0, 1, 0, 0, 0]:
                fing = cv2.imread(r"C:\Users\turbo\Documents\GitHub\handgesturepainting\1.jpg")
            if fingerup == [0, 1, 1, 0, 0]:
                fing = cv2.imread(r"C:\Users\turbo\Documents\GitHub\handgesturepainting\2.jpg")
            if fingerup == [0, 1, 1, 1, 0]:
                fing = cv2.imread(r"C:\Users\turbo\Documents\GitHub\handgesturepainting\3.png")
            if fingerup == [0, 1, 1, 1, 1]:
                fing = cv2.imread(r"C:\Users\turbo\Documents\GitHub\handgesturepainting\4.png")
            if fingerup == [1, 1, 1, 1, 1]:
                fing = cv2.imread(r"C:\Users\turbo\Documents\GitHub\handgesturepainting\5.jpg")
            if fingerup == [0, 0, 0, 0, 1]:
                fing = cv2.imread(r"C:\Users\turbo\Documents\GitHub\handgesturepainting\images.jpg")    
    
    
    fing = cv2.resize(fing, (220, 280))
    img[50:330, 20:240] = fing
    cv2.imshow("Video", img)
      
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
          
video.release()
cv2.destroyAllWindows()
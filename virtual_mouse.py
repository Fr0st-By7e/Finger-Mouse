import cv2
import hand_tracker_module as htm
import time
import numpy as np
import autopy

##################################
wCam, hCam = 640, 480
wScr, hScr = autopy.screen.size()
frameR = 100  # Frame Reduction
smoothening = 7
##################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
plocX, plocY = 0, 0
clocX, clocY = 0, 0

pT = 0

detector = htm.HandTracker(maxHands=1)

while True:
    # Find hand and landmark positions
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - int(1.5 * frameR)), (255, 0, 255), 2)  # Reduced frame

    # Get the tip of the index and middle fingers
    if len(lmList) != 0:
        xi, yi = lmList[8][1], lmList[8][2]  # Position of the index finger tip (id 8)
        xm, ym = lmList[12][1], lmList[12][2]  # Position of the middle finger tip (id 12)
        cv2.circle(img, (xi, yi), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (xm, ym), 15, (255, 0, 255), cv2.FILLED)

    # Check which fingers are up
        fingers = detector.fingersUp()

        # If only the index finger is up: Moving Mode
        if fingers[1] == 1 and fingers[2] == 0:
            # Convert Coordinates
            x3 = np.interp(xi, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(yi, (frameR, hCam - int(1.5 * frameR)), (0, hScr))

            # Smoothen Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # Move Mouse
            try:
                autopy.mouse.move(clocX, clocY)
                cv2.circle(img, (xi, yi), 15, (0, 255, 0), cv2.FILLED)

                plocX, plocY = clocX, clocY
            except:
                pass

        # If both index and middle fingers are up: Clicking Mode
        if fingers[1] == 1 and fingers[2] == 1:
            length, img, lineInfo = detector.findDistance(8, 12, img)
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()
                # Avoid double click
                time.sleep(0.5)


    # FPS Calculation
    cT = time.time()
    fps = 1/(cT-pT)
    pT = cT
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)


    # Display
    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):
        break
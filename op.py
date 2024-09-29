import time
import mediapipe as mp
import cv2 as cv
import pyautogui

camera = cv.VideoCapture(0)

mpHands = mp.solutions.hands

hands = mpHands.Hands()

Draw = mp.solutions.drawing_utils

while True:
    success, img = camera.read()
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            Draw.draw_landmarks(img, handlms, mpHands.HAND_CONNECTIONS)
            if(abs(handlms.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].x*img.shape[1] - handlms.landmark[mpHands.HandLandmark.THUMB_TIP].x*img.shape[1]) < 30):
                if (abs(handlms.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].y * img.shape[0] - handlms.landmark[mpHands.HandLandmark.THUMB_TIP].y * img.shape[0]) < 30):
                    pyautogui.press("right")
            if (abs(handlms.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].x * img.shape[1] - handlms.landmark[mpHands.HandLandmark.THUMB_TIP].x * img.shape[1]) < 30):
                if (abs(handlms.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].y * img.shape[0] - handlms.landmark[mpHands.HandLandmark.THUMB_TIP].y * img.shape[0]) < 30):
                    pyautogui.press("left")
                    print("left")


    cv.imshow("image", img)
    cv.waitKey(1)





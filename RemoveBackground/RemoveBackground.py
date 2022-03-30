import cv2
import numpy as np
cap=cv2.VideoCapture(0)
fg=cv2.createBackgroundSubtractorMOG2()

while True:
    _,frame = cap.read()
    fmask=fg.apply(frame)

    cv2.imshow('orginal',frame)
    cv2.imshow('fg',fmask)

    k=cv2.waitKey(27) & 0xFF
    if(k==27):
        break

cv2.destroyAllWindows()
cap.release()
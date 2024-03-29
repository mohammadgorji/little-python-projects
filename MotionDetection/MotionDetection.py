import cv2

video = cv2.VideoCapture("video.avi")

background = cv2.imread("background.png")
background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
background = cv2.GaussianBlur(background, (21, 21), 0)

while True:
    status, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    diff = cv2.absdiff(background, gray)

    thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)[1]

    cnts, res = cv2.findContours(thresh.copy(),
                                 cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 30000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    #cv2.imshow("Gray Video", gray)
    #cv2.imshow("Diff Video", diff)
    #cv2.imshow("Threshold Video", thresh)

    cv2.imshow("All Contours", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyWindows()


#thresh = cv2.dilate(thresh, None, iterations=2)

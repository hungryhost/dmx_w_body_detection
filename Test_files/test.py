import cv2

cap = cv2.VideoCapture('rtsp://172.18.191.159:554/12')
framecounter = 0
while True:
    ret, img = cap.read()
    if framecounter % 6 == 0:
        # Displaying the output Image
        cv2.imshow("Image", img)
        print(framecounter)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    framecounter += 1
cap.release()
cv2.destroyAllWindows()

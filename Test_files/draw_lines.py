import cv2
import imutils
import numpy as np


def drawGrid(pic, n, m, line_color=(0, 255, 0), thickness=1, type_=cv2.LINE_AA):
    pxstep = int(pic.shape[1] / n)
    pystep = int(pic.shape[0] / m)
    x = pxstep
    y = pystep
    while x < pic.shape[1]:
        cv2.line(pic, (x, 0), (x, pic.shape[0]), color=line_color, lineType=type_, thickness=thickness)
        x += pxstep

    while y < pic.shape[0]:
        cv2.line(pic, (0, y), (pic.shape[1], y), color=line_color, lineType=type_, thickness=thickness)
        y += pystep
    return


def makeGrid(pic, n, m):
    coordinate_matrix = np.zeros((n, m), dtype=(int, 2))
    pxstep = int(pic.shape[1] / n)
    pystep = int(pic.shape[0] / m)
    x = 0
    y = 0
    xlist = []
    ylist = []
    while x < pic.shape[1]:
        xlist.append(x)
        x += pxstep
    while y < pic.shape[0]:
        ylist.append(y)
        y += pystep
    return np.array(xlist), np.array(ylist)


def findNearest(xlist, ylist, center):
    xminlist = np.abs(np.subtract(xlist, center[0]))
    yminlist = np.abs(np.subtract(ylist, center[1]))
    x1 = xlist[np.argmin(xminlist)]
    y1 = ylist[np.argmin(yminlist)]
    x2 = xlist[np.argmin(xminlist)+1]
    y2 = ylist[np.argmin(yminlist)+1]
    return (x1, y1), (x2, y2)

center = (151, 350)
#cap = cv2.VideoCapture('rtsp://172.18.191.159:554/11')
cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    # Displaying the output Image
    xlist, ylist = makeGrid(img, 12, 9)
    print(findNearest(xlist, ylist, center))
    #cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break
cap.release()
cv2.destroyAllWindows()

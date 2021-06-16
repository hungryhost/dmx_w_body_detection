import body_decetor_yo as yo
import cv2
from DMXEnttecPro import Controller
import imutils

# cap = yo.cv2.VideoCapture('humans_1.mp4')
# cap = yo.cv2.VideoCapture('rtsp://172.18.191.159:554/12')
# cap = cv2.VideoCapture('rtsp://172.18.191.159:554/11')


cap = cv2.VideoCapture(0)


def drawGrid(pic, n, m, line_color=(0, 255, 0), thickness=1, type_=cv2.LINE_AA):
    pxstep = int(pic.shape[1] / n)
    pystep = int(pic.shape[0] / m)
    x = 0
    y = 0
    xlist = []
    ylist = []
    while x <= pic.shape[1]:
        cv2.line(pic, (x, 0), (x, pic.shape[0]), color=line_color, lineType=type_, thickness=thickness)
        xlist.append(x)
        x += pxstep

    while y <= pic.shape[0]:
        cv2.line(pic, (0, y), (pic.shape[1], y), color=line_color, lineType=type_, thickness=thickness)
        ylist.append(y)
        y += pystep
    return xlist, ylist


if __name__ == "__main__":
    # dmx = Controller('/dev/ttyUSB0')
    ret, frame = cap.read()
    xlist, ylist = drawGrid(frame, 4, 4)
    while True:
        ret, frame = cap.read()
        image = yo.tf.expand_dims(frame, 0)
        image = yo.tf.image.resize(image, (yo.size, yo.size)) / 255

        boxes, scores, classes, nums = yo.yolo(image)
        frame, xind, yind = yo.draw_outputs_v2(img=frame, outputs=(boxes, scores, classes, nums),
                                               class_names=yo.class_names, white_list=['person'], xlist=xlist,
                                               ylist=ylist)
        frame = yo.draw_outputs(img=frame, outputs=(boxes, scores, classes, nums),
                                class_names=yo.class_names, white_list=['person'])

        # dmx.set_channel(3, 100+xind+yind) # Sets DMX channel 1 to max 255
        # dmx.submit()
        #drawGrid(frame, 4, 4)
        yo.cv2.imshow('frame', frame)
        if yo.cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

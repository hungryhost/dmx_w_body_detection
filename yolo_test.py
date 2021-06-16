import body_decetor_yo as yo
import cv2

# cap = yo.cv2.VideoCapture('humans_1.mp4')
# cap = yo.cv2.VideoCapture('rtsp://172.18.191.159:554/12')
cap = cv2.VideoCapture('rtsp://172.18.191.159:554/11')


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


if __name__ == "__main__":
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        image = yo.tf.expand_dims(frame, 0)
        image = yo.tf.image.resize(image, (yo.size, yo.size)) / 255

        boxes, scores, classes, nums = yo.yolo(image)
        frame = yo.draw_outputs_v2(frame, (boxes, scores, classes, nums), yo.class_names, ['person'])
        drawGrid(frame, 6, 6)
        yo.cv2.imshow('frame', frame)
        if yo.cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

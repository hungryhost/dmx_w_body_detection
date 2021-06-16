import cv2
import imutils

# Initializing the HOG person
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# Reading the Image


cap = cv2.VideoCapture('rtsp://172.18.191.159:554/12')

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(40, 40)
    )
    # Resizing the Image
    image = imutils.resize(gray,
                           width=min(500, gray.shape[1]))

    # Detecting all humans
    (humans, _) = hog.detectMultiScale(image,
                                       winStride=(5, 5),
                                       padding=(3, 3),
                                       scale=1.21)
    # getting no. of human detected
    print('Human Detected : ', len(humans))

    # Drawing the rectangle regions
    for (x, y, w, h) in humans:
        cv2.rectangle(img, (x, y),
                      (x + w, y + h),
                      (0, 0, 255), 2)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (int(x - w / 2), int(y - h / 2)),
                      (int(x + w / 2), int(y + h / 2)),
                      (0, 0, 255), 2)

    # Displaying the output Image
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

import imutils
import cv2
from mtcnn import MTCNN

cap = cv2.VideoCapture('videodemo.mp4')
detector = MTCNN()
i = 0
while True:

    ret,frame = cap.read()
    frame = imutils.resize(frame, width=1200)
    output = detector.detect_faces(frame)
    count = 0
    for single_output in output:

        x,y,width,height = single_output['box']
        img_face = cv2.resize(frame[y + 3: y + height - 3, x + 3: x + width - 3], (64, 64))
        cv2.imwrite('train/images_{}.jpg'.format(count), img_face)
        count = count + 1
        cv2.rectangle(frame,pt1=(x,y),pt2=(x+width,y+height),color=(255,0,0),thickness=2)
    cv2.imshow('win',frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()
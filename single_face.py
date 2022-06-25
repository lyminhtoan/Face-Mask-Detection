from mtcnn import MTCNN
import cv2
import imutils

detector = MTCNN()

img = cv2.imread('imagedemo2.png')

output = detector.detect_faces(img)
#[{},{}...{}]
print(output)

for i in output:
    x,y,widht,height = i['box']

    left_eyeX,left_eyeY = i['keypoints']['left_eye']
    right_eyeX,right_eyeY = i['keypoints']['right_eye']
    noseX,noseY = i['keypoints']['nose']
    mouth_leftX,mouth_leftY = i['keypoints']['mouth_left']
    mouth_rightX,mouth_rightY = i['keypoints']['mouth_right']

    cv2.circle(img,center=(left_eyeX,left_eyeY),color=(255,0,0),thickness=3,radius=2)
    cv2.circle(img,center=(right_eyeX,right_eyeY),color=(255,0,0),thickness=3,radius=2)
    cv2.circle(img,center=(noseX,noseY),color=(255,0,0),thickness=3,radius=2)
    cv2.circle(img,center=(mouth_leftX,mouth_leftY),color=(255,0,0),thickness=3,radius=2)
    cv2.circle(img,center=(mouth_rightX,mouth_rightY),color=(255,0,0),thickness=3,radius=2)

    cv2.rectangle(img,pt1=(x,y),pt2=(x+widht,y+height),color=(255,0,0),thickness=3)
    cv2.rectangle(img,pt1=(noseX,noseY),pt2=(mouth_rightX,mouth_rightY),color=(0,255,0),thickness=2)
img = imutils.resize(img, width=800)
cv2.imshow('window',img)

cv2.waitKey(0)




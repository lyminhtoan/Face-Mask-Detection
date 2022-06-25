import cv2 as cv


def rescale_frame(frame, scale):    # works for image, video, live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def change_res(width, height):      # works only for live video
    capture.set(3, width)
    capture.set(4, height)


capture = cv.VideoCapture(0)    # integer to capture from webcam, path to capture video file

while True:
    isTrue, frame = capture.read()
    frame_resized = rescale_frame(frame, scale=.2)    # this line
    cv.imshow("Video", frame)
    # cv.imshow("Video Resized", frame_resized)
    if cv.waitKey(20) & 0xFF == ord("q"):       # press "q" key to exit loop
        break


capture.release()
cv.destroyAllWindows()
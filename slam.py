import cv2 as cv


def process_frame(img):
    cv.imshow('frame', img)


if __name__ == "__main__":
    cap = cv.VideoCapture('driving720slowed.mp4')

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break
        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

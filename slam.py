import cv2 as cv
import numpy as np


class FeatureExtractor():
    def __init__(self, img=None) -> None:
        self.img = img

    def extract(self, img, maxCorners=3000, qualityLevel=0.01, minDistance=5):
        self.img = img
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        corners = cv.goodFeaturesToTrack(
            gray, maxCorners, qualityLevel, minDistance)
        corners = np.intp(corners)

        return corners

    def imshow(self, corners):
        for i in corners:
            x, y = i.ravel()
            cv.circle(self.img, (x, y), 3, (0, 255, 0), -1)
        cv.imshow('frame', self.img)


if __name__ == "__main__":
    cap = cv.VideoCapture('driving720slowed.mp4')
    fe = FeatureExtractor()

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            feats = fe.extract(frame)
            fe.imshow(feats)
        else:
            break
        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

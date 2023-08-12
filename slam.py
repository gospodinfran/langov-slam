import cv2 as cv
import numpy as np


class FeatureExtractor():
    def __init__(self, img=None) -> None:
        self.img = cv.resize(img, (1280, 720)
                             ) if img is not None else None
        self.orb = cv.ORB_create(4000)

    def extract(self, img=None, maxCorners=4000, qualityLevel=0.01, minDistance=5):
        if img is not None:
            img = cv.resize(img, (1280, 720))
            self.img = img
        else:
            img = self.img
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        corners = cv.goodFeaturesToTrack(
            gray, maxCorners, qualityLevel, minDistance)

        kps = []
        for feat in corners:
            kp = cv.KeyPoint(x=feat[0][0], y=feat[0][1], size=20)
            kps.append(kp)
        des = self.orb.compute(img, kps)
        corners = np.intp(corners)

        return kps, des

    def draw_corners(self, corners):
        for i in corners:
            u, v = i.ravel()
            cv.circle(self.img, (u, v), 3, (0, 255, 0), -1)


def draw_kp(kp, img):
    for p in kp:
        u, v = map(lambda x: int(round(x)), p.pt)
        cv.circle(img, (u, v), 3, (0, 255, 0), -1)


def process_frame(frame):
    frame = cv.resize(frame, (1280, 720))
    kps, des = fe.extract(frame)
    draw_kp(kps, frame)
    cv.imshow('frame', frame)
    return kps, des


if __name__ == "__main__":
    cap = cv.VideoCapture('driving720slowed.mp4')
    fe = FeatureExtractor()

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            kps, des = process_frame(frame)
        else:
            break
        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

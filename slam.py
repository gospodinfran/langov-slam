import cv2 as cv
import numpy as np


class FeatureExtractor():
    def __init__(self):
        self.orb = cv.ORB_create(3000)
        self.bf = cv.BFMatcher()
        self.last = None

    def extract(self, img, maxCorners=3000, qualityLevel=0.01, minDistance=5):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        corners = cv.goodFeaturesToTrack(
            gray, maxCorners, qualityLevel, minDistance)

        kps = [cv.KeyPoint(x=f[0][0], y=f[0][1], size=20) for f in corners]
        kps, des = self.orb.compute(img, kps)

        matches = None
        if self.last is not None:
            matches = self.bf.match(des, self.last['des'])
        self.last = {'kps': kps, 'des': des}

        return kps, des, matches


def draw_kp(kp, img):
    for p in kp:
        u, v = map(lambda x: int(round(x)), p.pt)
        cv.circle(img, (u, v), 3, (0, 255, 0), -1)


def draw_matches():
    matches = sorted(matches, key=lambda x: x.distance)


def process_frame(frame):
    frame = cv.resize(frame, (1280, 720))
    kps, des, matches = fe.extract(frame)
    draw_kp(kps, frame)
    cv.imshow('frame', frame)
    return kps, des


if __name__ == "__main__":
    cap = cv.VideoCapture('driving720fast.mp4')
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

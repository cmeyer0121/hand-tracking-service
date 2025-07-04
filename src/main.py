from camera import Camera
from tracker import Tracker
from service import Service

import cv2 as cv


def main():
    camera = Camera(None)

    while True:
        frame = camera.get_frame()
        cv.imshow('Frame', frame)
        cv.waitKey(0)


    tracker = Tracker()
    service = Service()

    while True:
        frame = camera.get_frame()
        tracker.process_frame(frame)
        positions = tracker.get_positions()
        service.handle_requests()

if __name__ == "__main__":
    main()

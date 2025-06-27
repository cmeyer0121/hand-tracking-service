from camera import Camera
from tracker import Tracker
from service import Service



def main():
    camera = Camera()
    tracker = Tracker()
    service = Service()

    while True:
        frame = camera.get_frame()
        tracker.process_frame(frame)
        positions = tracker.get_positions()
        service.handle_requests()

if __name__ == "__main__":
    main()

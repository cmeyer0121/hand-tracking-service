# camera.py
import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2 as cv

class Camera:
    """
    Manages camera's physical attributes and its data.

    Attributes:
        model (object): The camera model.
        frame_rate (integer): Rate of frames per second
    """
    def __init__(self, model): # ctor
        self.model = model
        self.frame_rate = 30
        self.cap = cv.VideoCapture(0)

    def get_frame(self):
        ret, frame = self.cap.read()

        if not ret:
            print("Failed to read frame from camera")
            return
        
        return frame


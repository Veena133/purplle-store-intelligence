import cv2
from ultralytics import YOLO
from event_generator import generate_detection_event

class VideoProcessor:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def process(self, video_path):
        cap = cv2.VideoCapture(video_path)
        while True:
            success, frame = cap.read()
            if not success:
                break
            results = self.model(frame, classes=[0])
            for result in results:
                for box in result.boxes:
                    x1,y1,x2,y2 = map(int, box.xyxy[0])
                    confidence = float(box.conf[0])
                    event = generate_detection_event(x1,y1,x2,y2,confidence)
                    print(event)
        cap.release()

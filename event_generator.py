from datetime import datetime

def generate_detection_event(x1,y1,x2,y2,confidence):
    return {
        "event_type":"person_detected",
        "timestamp":datetime.utcnow().isoformat(),
        "bbox":{"x1":x1,"y1":y1,"x2":x2,"y2":y2},
        "confidence":confidence
    }

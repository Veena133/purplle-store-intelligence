class Tracker:
    def __init__(self):
        self.active_tracks = {}

    def update(self, track_id, bbox):
        self.active_tracks[track_id] = bbox
        return track_id

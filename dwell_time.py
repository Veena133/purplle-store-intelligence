import time

class DwellTime:
    def __init__(self):
        self.sessions = {}

    def start(self, track_id):
        self.sessions[track_id] = time.time()

    def end(self, track_id):
        return time.time() - self.sessions[track_id]

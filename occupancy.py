class OccupancyCounter:
    def __init__(self):
        self.current = 0

    def enter(self):
        self.current += 1

    def exit(self):
        self.current -= 1

    def get_count(self):
        return self.current

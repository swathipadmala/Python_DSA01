class carrentals:
    def __init__(self):
        self.queue = []
    def start_raid(self,cars):
        self.queue.insert(0,cars)
    def end_raid(self):
        self.queue.pop()
    def get_remaining(self):
        return self.queue[-1]
    def total_cars(self):
        print(str(self.queue))

cars = carrentals()
cars.start_raid("BMW")
cars.start_raid("Lamborgin")
cars.start_raid("Mini Cooper")
cars.start_raid("Swift")
cars.end_raid()
cars.get_remaining()
cars.total_cars()
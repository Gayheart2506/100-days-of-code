class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []
    
    def add_passenger(self, name):
        self.passenger.append(name)
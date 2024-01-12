class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.available_seats():
            return False
        self.passengers.append(name)
        return True
    
    def available_seats(self):
        return self.capacity - len(self.passengers)
    

flight = Flight(4)

persons = ["Gayheart", "Marvin", "Williams", "Leticia", "Matthew"]
for person in persons:
    on_board = flight.add_passenger(person)

    if on_board:
        print(f"sucessfully added {person} to flight.")
    else:
        print(f"There are no more seats avaiable for {person}")
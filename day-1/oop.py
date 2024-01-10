class Car_move():
    def __init__(self, petrol_tank, car_condition):
        self.petrol = petrol_tank
        self.status = car_condition

car1 = Car_move(100, "Good")
car2 = Car_move(90, "Bad")
print(car1.petrol)
print(car1.status)
print(car2.petrol)
print(car2.status)
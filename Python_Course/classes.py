# A class example in which we look at capacity and adding passengers based on the available capacity.

class flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passengers(self, name):
        if not self.open_seats():
            return False
        else:
            self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


f = flight(3)

passenger_names = ["Ali", "Waleed", "Ammar", "Maken"]

for people in passenger_names:
    if f.add_passengers(people):
        print(f"Added {people} in flight")
    else:
        print(f"{people} had no space.")

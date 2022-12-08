# Create flight class

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, person):
        # add a conditional statement to check if your able to add a passenger
        if not self.check_seats():
            return False
        passengers.append(person)
        return True

    
    def check_seats(self):
        self.capacity - len(self.passengers)

#create an istance of the object 
flights = Flight(3)

#create a list 
people = ["Adam", "Alex", "Aime", "Ant"]

for i in people:
    success = flights.add_passenger(i)
    if success:
        print(f"Space was avaliable for {i}")
    else:
        print(f"Space was not avaliable for {i}") 
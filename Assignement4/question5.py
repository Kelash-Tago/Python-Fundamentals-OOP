#inheritance

class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class Car(Vehicle):
    def __init__(self,seats,brand,model):
        super().__init__(brand,model)
        self.seats=seats
class Bike(Vehicle):
    def __init__(self,engine,brand,model):
        super().__init__(brand,model)
        self.engine=engine
        
bike=Bike("XYZ","CD",2025)
print("Bike details: ",bike.engine,bike.brand,bike.model)
        
# create a class with name vehicle(2 properties model type)-parent class
# sub classes with own names, car motorcycle
class vehicle:
    def __init__(self,model,type):
        self.model=model
        self.type=type

        def capacity(self):
            raise NotImplementedError("subclass to use this method")
class car(vehicle):
    def capacity(self):
        return "2000"
class motorcycle(vehicle):
    def capacity(self):
        return "2500"
car=car("toyota","premio")
print(car.model)
print(car.type)
print(car.capacity())
motorcycle=motorcycle("honda","ninja")
print(motorcycle.model)
print(motorcycle.type)
print(motorcycle.capacity())
class EmergencyVihcles : # Make the main class which from we will make the subclasses
    def __init__(self,fuel,max_fuel,delay_time): #attributes:fuel,max_fuel,delay_time
        self.fuel=fuel
        self.max_fuel=max_fuel
        self.delay_time=delay_time
    # we use Encapsulation to control how the data is accessed or changed inside the class 
    @property #getter method
    def fuel(self): #getting the amout of fuel for the first time
        return self._fuel
    @fuel.setter #setter method
    def fuel(self, value): #setting the amount of fuel and confirm to always be positive
        if value < 0:
            raise ValueError("Fuel must be positive")
        self._fuel = value
    def respond(self): #for each responf , the amount of fuel is reduced by 10
        if self.fuel<10: #if fuel is less than 10 and after cofirming it's a positive number , it will be 0
            self.fuel=0  
        else :
            self.fuel-=10
    def refuel(self): #refuel to max fuel
        self.fuel=self.max_fuel     
        print(f"The fuel is {self.fuel}")
# we use inheritance to do subclasses        
class Ambulance(EmergencyVihcles): # Ambulance is a subclass from EmergencyVehicles
    def __init__(self, fuel, max_fuel, delay_time):
        super().__init__(fuel, max_fuel, delay_time) 
    def respond(self):
        super().respond()    
        self.treat_patient()         
    def treat_patient(self): #method for treat patient
        print("Ambulance is treat a patient")

class PoliceCar(EmergencyVihcles): # Police car is a subclass from EmergencyVehicles
    def __init__(self, fuel, max_fuel, delay_time):
        super().__init__(fuel, max_fuel, delay_time)
    def respond(self):
         super().respond()
         self.arrest_suspect()     
    def arrest_suspect(self): #method for arresting suspects
        print("Police arrest suspect")

class FireFighter(EmergencyVihcles):# Firefighter is a subclass from EmergencyVehicles
    def __init__(self, fuel, max_fuel, delay_time):
        super().__init__(fuel, max_fuel, delay_time)
    def respond(self):
         super().respond() 
         self.extinguish_fire()    
    def rescue_civillain(self): #method for rescue civillain
        print("Rescue_civillain successfuly")
    def prepare(self): #method for prepare
        print("Prepare successfuly")
    def extinguish(self): # method for extinguish
        print("Extinguish successfuly")
    def extinguish_fire(self): #method for extinguish fire , we use abstraction to hide complicated details
        self.rescue_civillain()
        self.prepare()
        self.extinguish()

#using polymorphism:same method behaves differently depends on object
vehicles=[
    Ambulance(50,100,10),
    PoliceCar(10,100,10),
    FireFighter(20,100,10),
    Ambulance(0,100,10)
]
for vehicle in vehicles:
    if isinstance(vehicle,Ambulance): #to determine vehicle is in each subclass
        print(f"fuel before respond={vehicle.fuel}")
        vehicle.respond()
        print(f"fuel={vehicle.fuel}")
    elif isinstance(vehicle,PoliceCar):
        print(f"fuel before respond={vehicle.fuel}")
        vehicle.respond()
        print(f"fuel={vehicle.fuel}")
    elif isinstance(vehicle,FireFighter):
        print(f"fuel before respond={vehicle.fuel}")
        vehicle.respond()
        print(f"fuel={vehicle.fuel}")   
        vehicle.refuel() 

    else :
        print("Invalid vehicle")

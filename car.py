# Use the following link to make a seperate file called "main.py": https://github.com/Epic4773/Learning-Python/blob/main/41.%20Importing%20Classes%20and%20Modules%20(Car)
class Car:
  def __init__(self, make, model, year):
    # makes a Car object with the following attributes
    self.make = make
    self.model = model
    self.year = year
    self.odometer = 0
    self.tank = 0
        
  def describe_car(self):
    # returns a string that is the full name of the car.
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()
        
  def add_miles(self, miles):
    # increments miles to the odometer as long as miles is positive
    if miles < 0:
      print("it is illegal to roll back your odometer!")
    else:
      self.odometer += miles

  def show_miles(self):
    # prints a statement displaying the mileage of the car
    print(f"The {self.describe_car()} has {self.odometer} miles")
        
  def add_gas(self, gallons):
    # adds gallons to the tank as long as the tank size is not exceeded
    tank_size = 15 # amount of gallons the tank can hold
    if (self.tank + gallons) < tank_size:
      self.tank += gallons
    else:
      print("you are adding to many gallons to the tank!")
            
  def show_range(self):
    # prints a statement that shows how far the car can travel
    mileage = 30 # the mileage (in miles per gallon of fuel)
    miles = mileage*self.tank
    print(f"This car can travel {miles} miles before needing gas")
        
class Battery:
  # A simple class to model an electric car battery
  def __init__(self):
    # creates a battery object with one attribute
    self.charge = 0
        
  def charge_battery(self, kwh):
    # adds a charge in kilowatt-hours to a battery so long as it
    # does not exceed the charge limit
    battery_size = 75
    if (self.charge + kwh) < battery_size :
      self.charge += kwh
    else:
      print("Cannot charge battery past its limit!")
            
  def describe_battery(self):
    # returns a string that is a description of the car's batter
    description = f"This car has {self.charge} kilowatt-hours left in its battery"
    return description
        
class ElectricCar(Car):
    
  def __init__(self, make, model, year):
    super().__init__(make, model, year)
    self.battery = Battery()
        
  def add_fuel(self, gallons):
    print("You cannot put gas in an Electric Vehicle!")
        
  def show_range(self):
    mileage = 3.5 # miles per kwh
    miles = mileage*float(self.battery.charge)
    print(f"This car can travel {miles} miles before needing to charge its battery")

# # Slicing strings
# b = "Hello, World!"
# print(b[2:5])

# # Change to upper case
# a = "Hello, World!"
# print(a.upper())

class Car:
  def __init__(self, brand, model):
    self.brand = brand  # Attribute
    self.model = model  # Attribute
  
  def display_info(self):  # Method
    return f"{self.brand} {self.model}"

# Creating an object (instance of the Car class)
my_car = Car("Toyota", "Corolla")

# Output: Toyota Corolla
print(my_car.display_info())  
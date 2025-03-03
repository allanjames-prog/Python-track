
# Class (Blueprint)
class Car:  
    def __init__(self, brand, model):
        self.brand = brand  # Attribute
        self.model = model  # Attribute

# Creating different objects (instances)
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.brand)  # Toyota
print(car2.brand)  # Honda

# Example for flat screen
class flatScreen:
  def __init__(self, brand, size):
    # Attribute 1
    self.size = size 
    # Attribute 2
    self.brand = brand 

# Creating different instances (in otherwords objects)
flatScreen1 = flatScreen("Hisense", "50 inch")
flatScreen2 = flatScreen("Samsung", "32 inch")
flatScreen3 = flatScreen("Sony", "42 inch")

print(flatScreen1.brand)
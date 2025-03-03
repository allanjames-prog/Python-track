class Car:  # Class (Blueprint)
    def __init__(self, brand, model):
        self.brand = brand  # Attribute
        self.model = model  # Attribute

# Creating different objects (instances)
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.brand)  # Toyota
print(car2.brand)  # Honda

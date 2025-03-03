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
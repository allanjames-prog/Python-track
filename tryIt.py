# # Slicing strings
# b = "Hello, World!"
# print(b[2:5])

# # Change to upper case
# a = "Hello, World!"
# print(a.upper())

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand  # Attribute
#     self.model = model  # Attribute
  
#   def display_info(self):  # Method
#     return f"{self.brand} {self.model}"

# # Creating an object (instance of the Car class)
# my_car = Car("Toyota", "Corolla")

# # Output: Toyota Corolla
# print(my_car.display_info())  


"""
WRITING TO A FILE USING PYTHON

import os
# Function to write data to the file (Overwrites existing content)
def write_to_file():
  with open("myfile.txt", "w") as file:
    file.write("This is the text I intend to write in my file.\n")
    file.write("This is the second line.\n")
    file.write("This text overides what has been found there.")
  print("Data written to 'myfile.txt' successfully.")

# Function to append data to the file (Does not overwrite)
def append_to_file():
  with open("myfile.txt", "a") as file:
    file.write("Writing to a Text File in Python Python provides built-in functions to handle file operations like reading and writing. Below is a well-explained example of how to write to a .txt file in Python.\n")
  print("New data appended to 'myfile.txt'.")

# Function to read and display file contents
def read_file():
  if os.path.exists("myfile.txt"):
    with open("myfile.txt", "r") as file:
      content = file.read()
      print("\n=== File Contents ===")
      print(content)
  else:
        print("Error: 'myfile.txt' does not exist!")

# Main Execution
if __name__ == "__main__":
  # Step 1: Write to the file
  write_to_file() 
  # Step 2: Append new data 
  append_to_file() 
  # Step 3: Read and display file content
  read_file()      



# Open a file in write mode ('w')
file = open("example.txt", "w")

# Write some text to the file
file.write("Hello, this is the first line of text.\n")
file.write("This is the second line.\n")

# Always close the file after writing
file.close()




lines = ["First line.\n", "Second line.\n", "Third line.\n"]

with open("example.txt", "w") as file:  # Using 'with' automatically closes the file
  file.writelines(lines)




file_path = r"C:\Users\james\OneDrive\Documents\Workspace\my-text.txt"



# Other ways to define file paths.
# file_path = "C:\\Users\\james\\OneDrive\\Documents\\Workspace\\my-text.txt"

file_path = "C:/Users/james/OneDrive/Documents/Workspace/my-text.txt"

with open(file_path, "w") as file:
  file.write("Writing to a file in a specific location.")




from datetime import datetime

def log_event(event_message):
  with open("log.txt", "a") as log_file:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file.write(f"[{timestamp}] {event_message}\n")

# Example Usage
log_event("User logged in.")
log_event("File upload failed due to size limit.")




def save_user_data(name, age, email):
  with open("users.txt", "a") as file:
    file.write(f"Name: {name}, Age: {age}, Email: {email}\n")
    file.write(f"\n")

# Example Usage
save_user_data("John Doe", 25, "john@example.com")
save_user_data("Jane Smith", 30, "jane.smith@email.com")





import random
from datetime import datetime

def log_sensor_data():
  temperature = round(random.uniform(20, 30), 2)  # Simulated sensor data
  humidity = round(random.uniform(30, 60), 2)
  
  with open("sensor_data.txt", "a") as file:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"{timestamp}, Temperature: {temperature}°C, Humidity: {humidity}%\n")

# Example Usage
log_sensor_data()  # Simulate recording sensor data




def generate_report(sales_data):
  with open("sales_report.txt", "w") as file:
    file.write("=== Sales Report ===\n")
    file.write("Product | Quantity | Price\n")
    for product, (qty, price) in sales_data.items():
      file.write(f"{product} | {qty} | ${price:.2f}\n")

# Example Usage
sales = {
  "Laptop": (5, 1200.00),
  "Mouse": (15, 25.99),
  "Keyboard": (10, 45.50)
}
generate_report(sales)



def add_task(task):
  with open("todo.txt", "a") as file:
    file.write(f"- {task}\n")

# Example Usage
add_task("Finish Python project")
add_task("Prepare for the meeting at 3 PM")





"""
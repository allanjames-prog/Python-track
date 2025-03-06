# Multiple Lines at Once
lines = ["First line.\n", "Second line.\n", "Third line.\n"]
with open("example.txt", "w") as file:  # Using 'with' automatically closes the file
  file.writelines(lines)
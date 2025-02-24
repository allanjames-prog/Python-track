num1 = 0
num2 = 1

print(num1)
print(num2)

for i in range(8):
  num3 = num1 + num2
  num1 = num2
  num2 = num3

  print(num3 * "#")

# print(0)
# print(1)
# count = 2

# def fibonacci(prev1, prev2):
#     global count
#     if count <= 19:
#         newFibo = prev1 + prev2
#         print(newFibo)
#         prev2 = prev1
#         prev1 = newFibo
#         count += 1
#         fibonacci(prev1, prev2)
#     else:
#         return

# fibonacci(1,0)
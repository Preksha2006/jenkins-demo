def add(a, b):
    return a + b

num1 = 10
num2 = 20

result = add(num1, num2)

print("Welcome to Jenkins CI/CD Pipeline")
print("Number 1:", num1)
print("Number 2:", num2)
print("Sum:", result)

if result == 30:
    print("Test Passed!")
else:
    print("Test Failed!")

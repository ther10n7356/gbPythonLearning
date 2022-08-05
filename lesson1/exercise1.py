a = int(input("Enter first number: "))
opr = input("Enter operation (+-*/): ")
b = int(input("Enter second number: "))

if "+" == opr:
    result = a + b
elif "-" == opr:
    result = a - b
elif "*" == opr:
    result = a * b
elif "/" == opr:
    result = a / b
else:
    result = "Undefined operation!"

print("Result: ", result)

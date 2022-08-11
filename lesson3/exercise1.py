def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Делить на ноль нельзя!!!"


num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

print("Result: ", division(num1, num2))

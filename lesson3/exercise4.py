def my_func(x, y):
    print(f"Возведение числа {x} в степень {y} с использованием '**':", x ** y)

    n = x
    for i in range(1, abs(y)):
        n *= x

    print(f"Возведение числа {x} в степень {y} без использования '**':", (1 / n) if y < 0 else n)


num1 = int(input("Введите число: "))
num2 = int(input("Введите степень: "))

if num1 <= 0:
    print("Число должно быть положительным!")
else:
    my_func(num1, num2)

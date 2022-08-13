def fact(num):
    for i in range(1, num + 1):
        yield i


n = int(input("Введите факториал: "))

result = 1
print(f"Факториал числа {n}! вычисляется умножением чисел:")
for el in fact(n):
    result *= el
    print(el)

print("Результат: ", result)

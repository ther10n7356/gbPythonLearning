with open("text_5.txt", "w", encoding="utf-8") as obj:
    text = input("Введите числа разделенные пробелами: ")
    obj.write(text)
    result = 0
    try:
        for num in text.split():
            result += int(num)
    except ValueError:
        print("Invalid data!")

print("Сумма чисел в файле: ", result)

my_list = [7, 5, 3, 3, 2]
num = int(input("Введите новый элемент рейтинга: "))

if num > my_list[0]:
    my_list.insert(0, num)
elif num < my_list[len(my_list) - 1]:
    my_list.append(num)
else:
    for i in range(len(my_list) - 1):
        if my_list[i] >= num >= my_list[i + 1]:
            my_list.insert(i+1, num)
            break

print(f"Пользователь ввёл число {num}. Результат: {my_list}")

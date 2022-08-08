my_list = []

el = int(input("Введите количество товаров: "))

for i in range(el):
    print(f"Данные {i + 1}-го товара: ")
    name = input("Название: ")
    price = int(input("Цена: "))
    count = int(input("Количество: "))
    unit = input("Единицы: ")
    prd_dict = {"название": name, "цена": price, "количество": count, "ед": unit}
    my_tuple = (i + 1, prd_dict)
    my_list.append(my_tuple)
    i += 1
    print("Товар добавлен.")

ans = input("Собрать аналитику о товарах (y/n): ")
dict_analytic = {}
if ans == "y":
    for i in my_list[0][1].keys():
        dict_analytic.setdefault(i, [])

    for i in range(len(my_list)):
        my_dict = my_list[i][1]
        for j, v in my_dict.items():
            cnt = dict_analytic.get(j).count(v)
            if cnt == 0:
                dict_analytic.get(j).append(v)
    print(dict_analytic)
else:
    print(my_list)

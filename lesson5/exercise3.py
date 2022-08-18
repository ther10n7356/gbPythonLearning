limit = 20000.0
avg = 0.0
cnt_person = 0
with open("text_3.txt", "r", encoding="utf-8") as obj:
    print(f"Оклад меньше {limit}: ")
    for line in obj:
        my_list = line.split()
        if float(my_list[1]) < limit:
            print(my_list[0])
        avg += float(my_list[1])
        cnt_person += 1

print("Среднее значение оклада: ", avg/cnt_person)

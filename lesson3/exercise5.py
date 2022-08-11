def my_func(var_list, res):
    for i in range(len(var_list)):
        try:
            res += int(var_list[i])
        except Exception as err:
            if var_list[i] == "q":
                break
            else:
                print(err)
    return res


result = 0
print("Для выхода введите 'q', а для вывода результата нажмите 'Enter'.")
while True:
    my_list = input("Введите строку чисел: ").split()
    result = my_func(my_list, result)
    print(result)
    if "q" in my_list:
        break

def init_func(var_list):
    for i in range(len(var_list)):
        # простой вариант
        # var_list[i] = var_list[i].title()
        str_list = list(var_list[i].strip())
        str_list[0] = str_list[0].upper()
        var_list[i] = "".join(str_list)
    return var_list


my_list = input("Введите строку из слов разделенных пробелом: ").split()
print(" ".join(init_func(my_list)))

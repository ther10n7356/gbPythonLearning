def my_func(var_1, var_2, var_3):
    if var_1 >= var_2:
        return var_1 + max(var_2, var_3)
    else:
        return var_2 + max(var_1, var_3)


print(my_func(0, 2, 3))

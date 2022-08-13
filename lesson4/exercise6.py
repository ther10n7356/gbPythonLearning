from itertools import count, cycle


def get_count(limit_cnt):
    my_list = []
    for i in count(3):
        if limit_cnt < 0:
            break
        my_list.append(i)
        limit_cnt -= 1
    return my_list


def get_cycle(var_list, limit_cnt):
    my_list = []
    for el in cycle(var_list):
        if limit_cnt < 0:
            break
        my_list.append(el)
        limit_cnt -= 1
    return my_list


my_count = get_count(10)
print("Count iterator: ", my_count)

my_cycle = get_cycle(my_count, len(my_count)*2)
print("Cycle iterator: ", my_cycle)

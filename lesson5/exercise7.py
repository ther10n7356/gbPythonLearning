import json

dict_firm = {}
dict_list = []
with open("text_7.txt", "r", encoding="utf-8") as obj:
    average = 0
    firm_cnt = 0
    for line in obj:
        my_list = line.split()
        profit = int(my_list[2]) - int(my_list[3])
        print(profit)
        if profit > 0:
            average += profit
            firm_cnt += 1
        dict_firm.setdefault(my_list[0], profit)
    dict_list.append(dict_firm)
    dict_list.append({"average_profit": average/firm_cnt})
print(dict_list)

with open("text_77.json", "w", encoding="utf-8") as write_f:
    json.dump(dict_list, write_f, ensure_ascii=False, indent=4)

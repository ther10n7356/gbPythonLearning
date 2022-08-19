import re

my_dict = {}
with open("text_6.txt", "r", encoding="utf-8") as obj:
    for line in obj:
        name = re.match(r"^[A-Za-zА-Яа-я]+", line)
        hours = 0
        for i in line.split():
            result = re.match(r"\d*", i)
            if result[0] != "":
                hours += int(result[0])
        my_dict.setdefault(name[0], hours)
print(my_dict)

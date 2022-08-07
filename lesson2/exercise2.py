my_list = []

while True:
    el = input("Enter element, type EXIT to complete: ")
    if el.upper() == "EXIT":
        break
    my_list.append(el)

print("Before: ", my_list)
for i in range(len(my_list) - 1):
    print(i)
    if i % 2 != 0:
        continue
    list_el = my_list[i]
    my_list[i] = my_list[i+1]
    my_list[i+1] = list_el

print("After: ", my_list)

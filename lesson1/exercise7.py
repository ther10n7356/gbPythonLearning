a = int(input("Enter the result of the first day: "))
b = int(input("Enter expected result: "))

day = 1
while a < b:
    day += 1
    a += a/100*10
print(day)

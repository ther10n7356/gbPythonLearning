num = int(input("Enter a number: "))

m = 0
while num > 0:
    a = num % 10
    if a > m:
        m = a
    num = num // 10

print(m)

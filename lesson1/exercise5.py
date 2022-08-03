proceed = int(input("Enter proceed: "))
cost = int(input("Enter cost: "))

if proceed > cost:
    result = "Profit"
else:
    result = "Losses"
print(result)

seasons = {"Winter": [12, 1, 2], "Spring": [3, 4, 5], "Summer": [6, 7, 8], "Autumn": [9, 10, 11]}

month = int(input("Enter number of month: "))

if month < 1 or month > 12:
    print("Month must be between 1 and 12!")
else:
    for i in seasons:
        month_cnt = seasons.get(i).count(month)
        if month_cnt > 0:
            print(i)

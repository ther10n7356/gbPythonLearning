a = int(input("Enter time in seconds: "))

hours = a // 3600
minutes = (a % 3600)//60
seconds = a % 60
print(f"{hours:0>2}:{minutes:0>2}:{seconds:0>2}")

from sys import argv

script_name, production, bid, premium = argv

print("Выроботка в час: ", production)
print("Ставка в час: ", bid)
print("Премия: ", premium)

try:
    print("Итого: ", int(production)*int(bid) + int(premium))
except ValueError as err:
    print(err)

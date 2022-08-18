with open("text_1.txt", "w", encoding="utf-8") as obj:
    while True:
        text = input("Введите текст: ")
        if text == "":
            break
        print(text, file=obj)

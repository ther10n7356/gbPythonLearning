# pip install googletrans=4.0.0-rc1
from googletrans import Translator

translator = Translator()
with open("text_4.txt", "r", encoding="utf-8") as obj:
    with open("text_4_1.txt", "w", encoding="utf-8") as new_obj:
        for line in obj:
            result = translator.translate(line, dest='ru')
            print(result.text, file=new_obj)

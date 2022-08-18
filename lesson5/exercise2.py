with open("text_2.txt", "r", encoding="utf-8") as obj:
    word_cnt = 0
    line_cnt = 0
    for line in obj:
        line_cnt += 1
        word_cnt += len(line.split())

print("Count lines in file: ", line_cnt)
print("Count words in files: ", word_cnt)

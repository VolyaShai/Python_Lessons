with open("text_1.txt", "w", encoding="utf-8") as data_new:
    while True:
        string = input(" Введите строку для записи:")
        if not string:
            break
        print(string, file=data_new)

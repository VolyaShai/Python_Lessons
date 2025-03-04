string = input("Введите строку из нескольких слов:")
for ind, i in enumerate(string.split(), 1):
    if len(i) > 9:
        print(ind, i[0:10])
    else:
        print(ind, i)

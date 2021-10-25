rat = [7, 5, 3, 3, 2]
el_new = int(input("Введите свой рейтинг:"))
i = 0
for el in rat:
    if el >= el_new:
        i += 1
    else:
        break
rat.insert(i, el_new)
print(rat)

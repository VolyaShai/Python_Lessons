from random import randint

my_list = [randint(1, 100) for _ in range(20)]
with open("text_5.txt", "w", encoding="utf-8") as numbers:
    numbers.write(" ".join(map(str, my_list)))

print(f"Сумма чисел равна {sum(my_list)}")

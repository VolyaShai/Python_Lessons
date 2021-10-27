from itertools import count, cycle


def my_func():
    try:
        my_count = count(int(input("Введите целое число с какого стоит начать: ")))
        for num in range(9):
            print(f"Числа: {next(my_count)} Буквы: {next(my_cycle)}")
    except ValueError:
        print("Введите число!")


my_cycle = cycle("qwertyuiopasdfghjklzxcvbnm")
my_func()

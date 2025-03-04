def my_func(numb_1, numb_2, numb_3):
    try:
        # noinspection PyArgumentList
        numb_1, numb_2, numb_3 = int(numb_1), int(numb_2), int(numb_3)
        numbers = [numb_1, numb_2, numb_3]
        numbers.remove(min(numbers))
        return sum(numbers)
    except (ValueError, TypeError):
        print("Вводите числа!")


print(my_func(input("Введите первое число: "), input("Введите второе число: "), input("Введите третье число: ")))

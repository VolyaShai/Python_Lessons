def my_func(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return "Ошибка! Введите первое число положительное, второе отрицательное!"
        else:
            if y < 0:
                x = x * x
                y += 1
            x = 1 / x
            return x
    except (TypeError, ValueError):
        return "Ошибка! Вводите числа!"


numb_1 = input("Введите первое число положительное: ")
numb_2 = input("Введите второе число отрицательное: ")
print(round(my_func(numb_1, numb_2), 5))

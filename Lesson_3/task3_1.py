def division_func():
    numb_1 = float(input("Введите первое число: "))
    numb_2 = float(input("Введите второе число: "))
    try:
        division = numb_1 / numb_2
    except ZeroDivisionError as err_zero:
        print(err_zero)
    else:
        print(round(division, 2))


division_func()

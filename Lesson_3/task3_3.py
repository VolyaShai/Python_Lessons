def my_func(numb_1, numb_2, numb_3):
    numbers = [numb_1, numb_2, numb_3]
    try:
        numbers.remove(min(numbers))
        return sum(numbers)
    except TypeError:
        return "Вводите числа"


print(my_func(float(input("Введите первое число: ",)), float(input("Введите второе число: ")),
        float(input("Введите третье число: "))))

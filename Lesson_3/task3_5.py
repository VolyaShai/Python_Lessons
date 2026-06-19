def sum_all():
    sum_output = 0
    while True:
        enter_list = input("Введите строку чисел, разделенныъ пробелом:").split()
        for numb in enter_list:
            if numb == "q":
                return sum_output
            else:
                try:
                    sum_output += float(numb)
                    # sum_1 = sum(float(numb))
                except (TypeError, ValueError):
                    print("Вводите только ЧИСЛА через пробел")
        print(f"Сумма всех введенных чисел {sum_output}")


print(sum_all())

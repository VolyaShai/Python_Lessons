my_list = [33, "hi, my dear teacher!", True, [3.5, False, "Hello!"], (-2.3, [2, 4, 6], 3), {"name": "Volya", "age": 24}]
i = 0
n = 0
while i < (len(my_list)):
    print(type(my_list[i]))
    while i == 3 or i == 4:
        if n != 3:
            print(type(my_list[i][n]))
            n += 1
        else:
            n = 0
            break
    i += 1

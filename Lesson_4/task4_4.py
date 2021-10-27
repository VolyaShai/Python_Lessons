from random import randint

my_list = [randint(0, 20) for _ in range(0, 13)]
print(my_list)
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)

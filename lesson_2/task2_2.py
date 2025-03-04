my_list = list(input("Enter a number:"))
i = 1
while i < len(my_list):
    my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
    i += 2
print(my_list)
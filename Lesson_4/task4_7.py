def my_fact(n):
    fact = 1
    for numb in range(n + 1):
        yield f"{numb} = {fact}"
        fact *= numb + 1


for el in my_fact(int(input("Введите число: "))):
    print(el)

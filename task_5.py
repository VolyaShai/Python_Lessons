proceeds = float( input("Введите количество выручки:") )
costs = float( input("Введите количество издержек:") )
result = proceeds - costs
if result > 0:
    print(f"Фирма работает с прибылью {result:.2f}")
    rent = result / proceeds * 100
    print ( f"Рентабельность составляет {rent:.2f}")
    numb_emp = int(input("Введите количество сотрудников:"))
    profit_emp = rent / numb_emp
    print( f"Выручка на одного сотрудника составляет: {profit_emp:.2f}")
elif result < 0 :
   print("Фирма работает с убылью")

else:
    print("Прибыль равно 0, как и затраты")
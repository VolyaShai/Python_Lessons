with open("text_3.txt", encoding="utf-8") as salary_of_empl:
    my_dict = {line.split()[0]: float(line.split()[1]) for line in salary_of_empl}
    print(f"Средняя величина дохода - {sum(my_dict.values()) / len(my_dict)}\n"
          f"Сотрудники, получающие меньше 20 тыс: {[el[0] for el in my_dict.items() if el[1] < 20000 ]}")

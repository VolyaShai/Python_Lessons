class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"Полное имя сотрудника: {self.name} {self.surname}")

    def get_total_income(self):
        print(sum(self._income.values()))


a = Position("Bill", "Gates", "Shareholder", 1000000, 200000)
a.get_full_name()
print(a.position)
a.get_total_income()

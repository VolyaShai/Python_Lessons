class Cell:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"{self.number}"

    def __add__(self, other):
        print(f"Sum is:")
        return Cell(self.number + other.number)

    def __sub__(self, other):
        print(f"Subtraction is:")
        return Cell(self.number - other.number) if self.number - other.number > 0 \
            else "Error!The first cell has fewer cells than the second!"

    def __mul__(self, other):
        print(f"Multiply is:")
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        print(f"Truediv is:")
        return Cell(self.number // other.number)

    def make_order(self, row):
        return "\n".join(["*" * row for _ in range(self.number // row)]) + "\n" + "*" * (self.number % row)


cell_1 = Cell(29)
cell_2 = Cell(30)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(9))

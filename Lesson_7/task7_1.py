class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join("\t".join([f"{a}" for a in line]) for line in self.matrix)

    def __add__(self, other):
        return Matrix([[int(self.matrix[i][el]) + int(other.matrix[i][el]) for el in range(len(self.matrix[i]))]
                       for i in range(len(self.matrix))])


matrix_1 = Matrix([[1, 2, 3, 4], [3, 4, 4, 5], [5, 6, 6, 5]])
matrix_2 = Matrix([[7, 6, 6, 0], [6, 0, 1, 2], [1, 2, 3, 4]])
print(matrix_1)
print(matrix_2)
print(f"Сумма матриц\n{matrix_1 + matrix_2}")

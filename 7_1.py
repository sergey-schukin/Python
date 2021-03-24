# Реализовать класс  Matrix  (матрица). Обеспечить перегрузку конструктора класса (метод __init__() ),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица —  система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода  __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода  __add__() для реализации операции сложения двух
# объектов класса  Matrix  (двух матриц). Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = list_of_lists

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row))
                         for row in self.matrix)

    def __add__(self, other):
        result_matrix = []
        for i in range(len(self.matrix)):
            result_matrix.append([])
            for j in range(len(self.matrix[0])):
                result_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(result_matrix)


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[10, 12], [13, 41], [15, 6]])

print(matrix_1)
print("")
print(matrix_2)
print("")
print(matrix_1 + matrix_2)

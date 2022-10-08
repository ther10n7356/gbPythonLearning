from random import randint


class Matrix:

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        result = ""
        for i in self.matrix_list:
            result += " ".join(map(str, i)) + "\n"
        return result

    def __add__(self, other):
        new_matrix = self.matrix_list.copy()
        for i in range(len(self.matrix_list)):
            for j in range(len(self.matrix_list[i])):
                new_matrix[i][j] = self.matrix_list[i][j] + other.matrix_list[i][j]
        return Matrix(new_matrix)


def get_rand_matrix(length, width):
    new_matrix = []
    for i in range(length):
        my_list = []
        for j in range(width):
            my_list.append(randint(1, 100))
        new_matrix.append(my_list)
    return new_matrix


my_list_1 = get_rand_matrix(4, 2)
my_list_2 = get_rand_matrix(4, 2)
matrix_1 = Matrix(my_list_1)
matrix_2 = Matrix(my_list_2)
print("Первая матрица: ")
print(matrix_1)
print("Вторая матрица: ")
print(matrix_2)
print("Новая матрица: ")
print(matrix_1 + matrix_2)

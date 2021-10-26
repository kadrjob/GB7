class Matrix:

    def __init__(self, data):
        self.data = data

    def matrix_to_str(self, matrix):
        res = ''
        for x, y, z in matrix:
            res += f'{x} {y} {z}\n'
        return res

    def __str__(self):
        return self.matrix_to_str(self.data)

    def __add__(self, other):
        result = list(map(sum, zip(*i)) for i in zip(self.data, other.data))
        return self.matrix_to_str(result)


my_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
my_matrix1 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print(my_matrix)
print(my_matrix+my_matrix1)

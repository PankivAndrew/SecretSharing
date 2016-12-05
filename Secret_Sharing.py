import random
import numpy
import work_with_matrix


class Secret:
    def __init__(self, secret):
        self.secret = secret

    def choose_secret_vector(self):
        pass

    def genetare_vect_a(self, number, size):
        # while not self.check_independency(vectors):
        vectors = [[[], []], [[], []], [[], []], [[], []], [[], []]]
        while not self.check_independency(vectors):
            vectors = [[[], []], [[], []], [[], []], [[], []], [[], []]]
            for i in range(number // 2):
                for g in range(2):
                    for j in range(size):
                        vectors[i][g].append(random.randint(0, 1))

        return vectors

    def check_independency(self, matrix):
        if matrix != [[[], []], [[], []], [[], []], [[], []], [[], []]]:
            for i in range(1, len(matrix) - 2):
                for j in range(i + 1, len(matrix) - 1):
                    for k in range(j + 1, len(matrix)):
                        if self.determinant([matrix[i][0],matrix[i][1], matrix[j][0], matrix[j][1], matrix[k][0],  matrix[k][1]]) == 0:
                            return False
            return True
        else:
            return False
    def determinant(self, matrix):
        return numpy.linalg.det(matrix)

a = Secret(1)
print(a.genetare_vect_a(10, 6))#Перевір цей виклик, він повертає 1 векторів, треба забити в калькулятор і перевірити чи

import random

import work_with_matrix


class Secret:
    def __init__(self, secret):
        self.secret = secret

    def choose_secret_vector(self):
        pass

    def genetare_vect_a(self, number, size):
        # while not self.check_independency(vectors):
        vectors = [[[], [],1], [[], [],2], [[], [],3], [[], [],4], [[], [],5]]
        for i in range(number // 2):
            for g in range(2):
                for j in range(size):
                    vectors[i][g].append(random.randint(0, 1))
        self.check_independency(vectors)
        return vectors

    def check_independency(self, matrix):
        if matrix:
            for i in range(1, len(matrix) - 2):
                for j in range(i + 1, len(matrix) - 1):
                    for k in range(j + 1, len(matrix)):

                        a = [matrix[i], matrix[j], matrix[k]]
                        print(a)

        else:
            return False


a = Secret(1)
a.genetare_vect_a(10, 6)

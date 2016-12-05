import random
import work_with_matrix

class Secret:

    def __init__(self, secret):
        self.secret = secret

    def choose_secret_vector(self):
        pass
    def genetare_vect_a(self, number, size):
        vectors = []
        while not self.check_independency(vectors):
            vectors = []
            for i in range(number):

                vectors.append([])
                for j in range(size):
                  vectors[i].append(random.randint(0,1))
        return vectors
    def check_independency(self, matrix):
        if matrix != []:
            for i in range(len(matrix) - 2):
                for j in range(i + 1, len(matrix) - 1):
                    for k in range(j + 1, len(matrix)):

                        a = [matrix[i], matrix[j], matrix[k]]
                        if not work_with_matrix.check_matrix(a):
                            print('qwerftgyhujikljhgfghjgf')
                            return False
            return True
        else:
            return False

a = Secret(1)
print(a.genetare_vect_a(5,3))
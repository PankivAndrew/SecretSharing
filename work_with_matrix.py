def check_matrix(matrix):
    tmp = [0] * len(matrix[0])
    if type(to_reduced_row_echelon_form(matrix)) != bool:
        for line in to_reduced_row_echelon_form(matrix):
            if line == tmp:
                return False
        return True
    return False


def number_of_rows(matrix):
    return len(matrix)


def number_of_colums(matrix):
    return len(matrix[0])


def to_reduced_row_echelon_form(matrix):
    if not matrix:
        return False
    lead = 0
    row_сount = number_of_rows(matrix)
    column_сount = number_of_colums(matrix)
    for r in range(row_сount):
        if lead >= column_сount:
            return False
        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == row_сount:
                i = r
                lead += 1
                if column_сount == lead:
                    return False
        matrix[i], matrix[r] = matrix[r], matrix[i]
        lv = matrix[r][lead]
        matrix[r] = [mrx / float(lv) for mrx in matrix[r]]
        for i in range(row_сount):
            if i != r:
                lv = matrix[i][lead]
                matrix[i] = [iv - lv * rv for rv, iv in zip(matrix[r], matrix[i])]
        lead += 1
    final_matr = []
    for i in matrix:
        a = []
        for j in i:
            a.append(round(j, 1))
        final_matr.append(a)
    return final_matr

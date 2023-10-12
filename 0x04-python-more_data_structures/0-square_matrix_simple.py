def square_matrix_simple(matrix=[]):
    return list(map(lambda row: list(map(lambda e: e ** 2, row)), matrix))

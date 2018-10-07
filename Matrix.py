import random


def random_matrix(m, n):
    matrix = []
    for i in xrange(m):
        row = []
        n_alt = n
        while n_alt > 0:
            a = random.randint(0, 9)
            row.append(a)
            n_alt -= 1
        matrix.append(row)
    return matrix


def identity_matrix(m):
    I = []
    for i in xrange(m):
        new_row = m * [0]
        new_row[i] = 1
        I.append(new_row)
    return I


def show_matrix(matrix):
    for row in matrix:
        print row


def matrix_length(matrix):
    return len(matrix[0])


def matrix_width(matrix):
    return len(matrix)


def transpose_matrix(matrix):
    transposed_matrix = []
    for n in xrange(matrix_length(matrix)):
        new_row = []
        for row in matrix:
            new_row.append(row[n])
        transposed_matrix.append(new_row)
    return transposed_matrix


def vector_addition(vector1, vector2):
    if len(vector1) != len(vector2):
        print "Wrong dimensions"
    else:
        new_vector = []
        for n in xrange(len(vector1)):
            a = vector1[n] + vector2[n]
            new_vector.append(a)
        return new_vector


def scalar_vector(vector, a):
    new_vector = []
    for element in vector:
        alpha = a * element
        new_vector.append(alpha)
    return new_vector


def scalar_product(vector1, vector2):
    if len(vector1) != len(vector2):
        print "Wrong dimensions"
    else:
        product = 0
        for n in xrange(len(vector1)):
            a = vector1[n] * vector2[n]
            product += a
        return product


def matrix_addition(matrix1, matrix2):
    if matrix_length(matrix1) != matrix_length(matrix2):
        print "Wrong dimensions"
    elif matrix_width(matrix1) != matrix_width(matrix2):
        print "Wrong dimensions"
    else:
        new_matrix = []
        for n in xrange(matrix_width(matrix1)):
            new_row = vector_addition(matrix1[n], matrix2[n])
            new_matrix.append(new_row)
        return new_matrix


def scalar_matrix(matrix, a):
    new_matrix = []
    for row in matrix:
        new_row = scalar_vector(row, a)
        new_matrix.append(new_row)
    return new_matrix


def matrix_product(matrix1, matrix2):
    if matrix_length(matrix1) != matrix_width(matrix2):
        print "Wrong dimensions"
    else:
        new_matrix = []
        for row in matrix1:
            new_row = []
            for column in transpose_matrix(matrix2):
                alpha = scalar_product(row, column)
                new_row.append(alpha)
            new_matrix.append(new_row)
        return new_matrix


def nullify_element(vector1, vector2, n):
    if vector2[n] == 0:
        return vector2
    else:
        return vector_addition(vector1, scalar_vector(vector2, -1.0 * vector1[n] / vector2[n]))


def row_echelon(matrix):
    new_matrix = matrix
    for m in xrange(matrix_width(matrix) - 1):
        for n in range(m + 1, matrix_width(matrix) + 1):
            try:
                new_matrix[n] = nullify_element(matrix[m], matrix[n], m)
            except IndexError:
                pass
    return new_matrix


def extract_diagonal(matrix):
    new_matrix = matrix
    for n in xrange(matrix_width(matrix)):
        for i in xrange(matrix_length(matrix)):
            if n != i:
                (matrix[n])[i] = 0
    return new_matrix

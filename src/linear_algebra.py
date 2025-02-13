import math

""" vectors """

"""adds two vectors componentwise"""
def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v,w)]

"""substract two vectors componentwise"""
def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v,w)]

"""adds corresponding elements"""
def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

"""mulyiply each element by a scalar"""
def scalar_multiply(c, v):
    return [c * v_i for v_i in v]

"""compute vector mean"""
def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

"""compute dot product
    v_1 * w_1 + ... + v_n * w_n
"""
def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

"""compute sum of squares"""
def sum_of_squares(v):
    return dot(v, v)

"""compute the magnitude or length"""
def magnitude(v):
    return math.sqrt(sum_of_squares(v))

"""squared distance between two vectors"""
def squared_distance(v,w):
    return sum_of_squares(vector_subtract(v,w))

"""distance between two vectors"""
def distance(v,w):
    return math.sqrt(squared_distance(v,w))


""" matrices """

"""shape of matrix"""
def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

"""extract the i'th row from matrix"""
def get_row(A, i):
    return A[i]

"""extract the i'th column from matrix"""
def get_column(A, i):
    return [A_row[i] for A_row in A]

"""create a NxM matrix using the function fnc"""
def create_matrix(n, m, fnc):
    return [[fnc(i,j) for j in range(m)]
            for i in range(n)]

"""fnc functions for matrix patterns"""
"""diagonal function"""
def is_diagonal(i, j):
    """or identity matrix"""
    return 1 if i == j else 0

import numpy as np

def validate_matrix(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError("Matrix is not a numpy array")
    if matrix.ndim > 2: # Number of array dimensions.
        raise ValueError("Matrix is not 2-dimensional")
    if matrix.size == 0: # Number of elements in the array.
        raise ValueError("Matrix is empty")
    if matrix.size == 1:
        raise ValueError("Matrix is a scalar")
    if matrix.size == 2:
        raise ValueError("Matrix is a vector")
    # if matrix.size > 4:
    #     raise ValueError("Matrix is too large")

def validate_operation(operation):
    if not isinstance(operation, str):
        raise ValueError("Operation is not a string")

def validate_addition(matrix1, matrix2):
    if matrix1.shape != matrix2.shape:
        raise ValueError("Matrices have different shapes")
    
def validate_multiplication(matrix1, matrix2):
    if matrix1.shape[1] != matrix2.shape[0]:
        raise ValueError("Matrices have incompatible shapes")
    
def validate_transposition(matrix):
    if matrix.ndim != 2:
        raise ValueError("Matrix is not 2-dimensional")
    
def validate_matrix_operation(matrix1, matrix2, operation):
    validate_matrix(matrix1)

    if not "T" in operation:
        validate_matrix(matrix2)

    validate_operation(operation)
    if "+" in operation:
        validate_addition(matrix1, matrix2)
    if "*" in operation:
        validate_multiplication(matrix1, matrix2)
    if "'" in operation:
        validate_transposition(matrix1)
        validate_transposition(matrix2)

def matrix_operation(matrix1, matrix2, operation):
    validate_matrix_operation(matrix1, matrix2, operation)
    return eval(operation)

def matrix_addition(matrix1, matrix2):
    return matrix_operation(matrix1, matrix2, "matrix1 + matrix2")

def matrix_multiplication(matrix1, matrix2):
    return matrix_operation(matrix1, matrix2, "np.dot(matrix1, matrix2)")

def matrix_transposition(matrix):
    return matrix_operation(matrix, None, "matrix1.T")

# Testy
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

print(matrix_addition(matrix1, matrix2))
print("\r")
print(matrix_multiplication(matrix1, matrix2))
print("\r")
print(matrix_transposition(matrix1))
print("\r")
print(matrix_transposition(matrix2))
print("\r")

# Błędy
try:
    matrix_addition(matrix1, np.array([[1, 2, 3], [4, 5, 6]]))
except ValueError as e:
    print(e)

try:
    matrix_multiplication(matrix1, np.array([[1, 2, 3], [4, 5, 6]]))
except ValueError as e:
    print(e)

try:
    matrix_multiplication(matrix1, np.array([[1, 2], [3, 4], [5, 6]]))
except ValueError as e:
    print(e)
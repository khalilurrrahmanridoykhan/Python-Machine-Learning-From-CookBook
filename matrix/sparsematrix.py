import numpy as np
from scipy import sparse

# Crate a matrix
matrix = np.array([
    [1,0,2],
    [2,1,0],
    [0,1,3]
])
matrix_1 = np.array([
    [0,0],
    [0,1],
    [3,0]
])
# Matrix with matrix data structure
matrix_object = np.matrix([
[1,2],
[1,2],
[1,2]
])




# Crate compressed sparse row (CSR) matrix
matrix_sparse = sparse.csr_matrix(matrix_1)
print(matrix_sparse)
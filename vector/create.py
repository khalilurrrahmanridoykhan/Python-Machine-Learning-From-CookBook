import numpy as np

# One-dimentional array is a vector
vector_row = np.array([1,2,3])
vector_column = np.array([[1],[2],[3]])

# Two-dimentional array is a Matrix 
matrix = np.array([
    [1,2],
    [5,3],
    [6,4]
    ])

select_al_elemtnt_vector = vector_column[1:]
select_all_element_matrix = matrix[:2,:]

# View Numner of Row & Column
x = matrix.shape
y = vector_row.shape

# View Number of Elements ( row * column)
size = matrix.size
# View Numnber of Dimensions
dimensions = matrix.ndim

# Operations
add_100 = lambda i: i + 100
# Create Vectorized Function
vectorized_add_100 = np.vectorize(add_100)
# Apply function to add elements in matrix
apply= vectorized_add_100(matrix)
# Anonter way to add number
anoter_add =  matrix + 100





print(anoter_add)

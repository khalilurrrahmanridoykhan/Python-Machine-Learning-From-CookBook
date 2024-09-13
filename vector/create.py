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





print(select_all_element_matrix)

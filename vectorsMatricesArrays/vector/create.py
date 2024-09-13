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

max = np.max(matrix)
min = np.min(matrix)
max_row = np.max(matrix, axis=1)
max_column = np.max(matrix, axis=0)

mean = np.mean(matrix)
variance = np.var(matrix)
sgandard_deviaction = np.std(matrix)
mean_each_column = np.mean(matrix, axis=0)

resheap = matrix.reshape(2,3)
resheap_as_meny_i_want = matrix.reshape(1,-1)
reshape_one_d_array = matrix.reshape(size)

transposing = matrix.T
matrixnew = np.array([
    [1,2],
    [5,3],
    [6,4]
    ]).T

# With Flattening We can make a One-dimensional array
make_one_d =  matrix.flatten()

# Rank of a Matrix = Numner of Colums are Independent Here
rank = np.linalg.matrix_rank(matrix)

threedmatrinx = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
# Find The Determinant of A matrix
determinant = np.linalg.det(threedmatrinx)
diagonal = threedmatrinx.diagonal()
diagonal_above = threedmatrinx.diagonal(offset=1)
diagonal_below = threedmatrinx.diagonal(offset=-1)

# Trace of a Matrix = Sum of Diagonal of a matrix
trace = threedmatrinx.trace()

# Dot Product
dot_product = np.dot(vector_row,vector_row)
# Adding and Subttracting Matrix
add = np.add(threedmatrinx,threedmatrinx)
subtraction = np.subtract(threedmatrinx,threedmatrinx)
# Multipying Matrix
multipy = threedmatrinx @ threedmatrinx;
inverting = np.linalg.inv(threedmatrinx)
inverting_aonther_way = threedmatrinx @ np.linalg.inv(threedmatrinx)

# Random Values
np.random.seed(0)
# random between 0.0 t and 1.0
firstrandom = np.random.random(3)
# Random Numner with the mean 0.0
fiverandom = np.random.normal(0.0, 1.0, 3)
# Random Between 1 to 10
secendrandom = np.random.randint(0,11,3)
# Random number form a logistic distribtion with mean 0.0 and scale of 1.0
threedrandom = np.random.logistic(0.0, 1.0,3)
# Random getterthen or equal of 3 numnbers
fourrandom = np.random.uniform(1.0, 2.0, 3)

print(fiverandom)

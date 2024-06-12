# Import required package
import numpy as np

# # Define your matrix
# Taking a 3 * 3 matrix
A = np.array([[1, 2, 3],
              [4, 6, 6],
              [5, 8, 14]])

# Calculating the inverse of the matrix
print(np.linalg.inv(A))
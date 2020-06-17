"""Using NumPy create random vector of size 20 having only float in the range 1-20.
 Then reshape the array to 4 by 5
 Then replace the max in each row by 0(axis=1) """

# import numpy library
import numpy as np

# create a random vector of range 1-20 and size 20
a = (np.random.randint(1, 20, 20))

# display the random vector
print("Random vector of size 20 having float in the range 1-20:\n", a)

# reshape the random vector to 4 by 5 array
b = (a.reshape(4, 5))

# display the reshaped vector
print("Reshaped array to 4 by 5:\n", b)

# Find the maximum value in each row
x = (np.max(b, axis=1))

# Reshape the vector to column of size 1
y = x.reshape(-1, 1)

# Replace the max value in each row to 0 and display the final result of 4 by 5 array
print("Resultant 4 by 5 array with max value in each row is replaced with 0:\n", np.where(b == y, 0, b))
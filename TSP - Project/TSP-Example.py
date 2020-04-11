# pip install tsp in command line
# Check Environment in bottom left

import tsp

mat = [[  0,   1, 1, 1.5],
       [  1,   0, 1.5, 1],
       [  1, 1.5,   0, 1],
       [1.5,   1,   1, 0]]  # Distance Matrix
r = range(len(mat))
# Dictionary of distance
dist = {(i, j): mat[i][j] for i in r for j in r}
print(r)
print(dist)
print(tsp.tsp(r, dist))
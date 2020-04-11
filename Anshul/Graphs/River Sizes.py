matrix =[[1,0,0,1,0],
        [1,0,1,0,0],
        [0,0,1,0,1],
        [1,0,1,0,1],
        [1,1,1,1,0],
        [1,0,1,1,0]]

# Not Complete
# Solving via dictionary

def check(i,j,d):
    if j!=0 and i!=0 and matrix[i][j-1] == 1 and matrix[i-1][j] ==1:
        d[str([i,j])] = d[str([i,j-1])]+d[str([i-1,j])]+1
    elif matrix[i-1][j] == 1:
        if matrix[i-1][j+1] == 1:
            k=j+1
            while d[i-1][k] != 0 or k == len(matrix[0]):
                k+=1
            if d[i-1][k] == 0:d[str([i-1,k-1])] = d[str([i-1,k-1])]+1
            else:d[str([i-1,k])] = d[str([i-1,k])]+1
        else:
            d[str([i,j])] = d[str([i,j-1])]+1
            d[str([i,j-1])] = 0
    elif matrix[i-1][j] ==1 :
        d[str([i,j])] = d[str([i-1,j])]+1
        d[str([i-1,j])] = 0


def riverSize(matrix):
    d = {}
    array = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):   # O(n)
            if matrix[i][j] == 1:
                d[str([i,j])] = 1
                check(i,j,d)
    print(d)
    for i in d:
        if d[i] != 0: array.append(d[i])   # O(n)
    return array

print(riverSize(matrix))


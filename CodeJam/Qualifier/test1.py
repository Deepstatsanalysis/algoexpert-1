n = int(input()) 
testCase = []
for i in range(n):
    minRow=[]
    m = int(input())  
    for j in range(m):
        minRow.append(list(map(int,input().split())))
    testCase.append(minRow)

# 1 2 3 2
# 4 5 6 7
# 7 5 3 1
# 5 6 2 1

def solve(matrix):
    diagonal = 0
    row = 0
    col = 0
    for i in range(len(matrix[0])):
        rowd = {}
        cold = {}
        rowTest = False
        colTest = False
        for j in range(len(matrix[0])):
            if i == j:
                diagonal += matrix[i][j]
            if rowTest == False:
                if matrix[i][j] not in rowd:
                    rowd[matrix[i][j]] = i
                else:
                    rowTest = True
            if colTest == False:
                if matrix[j][i] not in cold:
                    cold[matrix[j][i]] = j
                else:
                    colTest = True
        if rowTest == True: row += 1
        if colTest == True: col += 1
    k = str(diagonal)+' '+str(row)+' '+str(col)
    return k


for i,e in enumerate (testCase):
    print('Case #'+str(i+1)+':',solve(e))
            
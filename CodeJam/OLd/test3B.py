n = int(input()) 
testCase = []
for i in range(n):
    minRow=[]
    m = int(input())  
    for j in range(m):
        minRow.append(list(map(int,input().split())))
    testCase.append(minRow)

def sortIt(matrix, varA, varB,ans):
    d ={}
    for i in range(len(matrix)):
        d[i] = matrix[i]
    matrix.sort()
    print(matrix)
    a = [matrix[0]]
    b = []
    for i in range(len(matrix)-1):
        if matrix[i+1][0] < matrix[i][1]:
            b.append(matrix[i+1])
            ans+=varB
        else:
            a.append(matrix[i+1])
            ans+=varA
    if b:
        if len(a) > 1:
            sortIt(a,'X','Y','X')
        if len(b) > 1:
            sortIt(b,'X','Y','X')
    return ans


for i,e in enumerate (testCase):
    print('Case #'+str(i+1)+':',sortIt(e,'J','C','J'))



# 4
# 3
# 360 480
# 420 540
# 600 660
# 3
# 0 1440
# 1 3
# 2 4
# 5
# 99 150
# 1 100
# 100 301
# 2 5
# 150 250
# 2
# 0 720
# 720 1440


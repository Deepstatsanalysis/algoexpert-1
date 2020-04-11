def sortIt(matrix):
    ans = 'J'
    run = ''
    rangeJ = [matrix[0]]
    rangeC = []
    for i in range(1,len(matrix)):  #[[360, 480],[420, 540],[600, 660]]  JCJ
        tempValue = ''
        for k in rangeJ:    # rangeJ = [[360, 480],[600, 660]]
            if matrix[i][0] >= k[1] and matrix[i][1] >= k[1]:
                tempValue='J'
            elif matrix[i][1] <= k[0] and matrix[i][0] <= k[0]:
                tempValue='J'
            else:
                run = 'TestC'
                break
        if run == 'TestC':    #rangeC = [[420,540]]
            run = ''
            if rangeC == [] : 
                rangeC.append(matrix[i])
                tempValue='C'
            else:
                for m in rangeC:
                    if matrix[i][0] >= m[1] and matrix[i][1] >= m[1]:
                        tempValue='C'
                    elif matrix[i][1] <= m[0] and matrix[i][0] <= m[0]:
                        tempValue='C'
                    else:
                        ans = 'IMPOSSIBLE'
                        break
            
            if ans != 'IMPOSSIBLE' : rangeC.append(matrix[i]) 
        else:
            rangeJ.append(matrix[i])
        if ans == 'IMPOSSIBLE':
            break 
        else : 
            ans+=tempValue

    return ans

n = int(input()) 
testCase = []
for i in range(n):
    minRow=[]
    m = int(input())  
    for j in range(m):
        minRow.append(list(map(int,input().split())))
    print('Case #'+str(i+1)+':',sortIt(minRow))
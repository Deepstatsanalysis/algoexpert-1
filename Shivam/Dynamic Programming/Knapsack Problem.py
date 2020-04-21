def knapsack(item,cap):
    array=[[0 for i in range(0,cap+1)] for y in range(0,len(item)+1)]
    for i in range(1,len(item)+1):
        currweight=item[i-1][1]
        currvalue=item[i-1][0]

        for j in range(0,cap + 1):
            if currweight> j:
                array[i][j]=array[i-1][j]

            else:
                array[i][j]=max(array[i-1][j],array[i-1][j-currweight]+currvalue)

    return [array[-1][-1],getitems(array,item)]



def getitems(array,item):
    seq=[]
    i=len(array)-1
    j=len(array[0])-1
    while i>0:
        if array[i][j] == array[i-1][j]:
            i-=1
        else:
            seq.append(i-1)
            j-=item[i-1][1]
            i-=1
        if j==0:
            break
    return list(reversed(seq))  


print(knapsack([[1,2],[4,3],[5,6],[6,7]],10))
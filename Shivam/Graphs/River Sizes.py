def RiverSizes(matrix):
    final=[]
    vischeck=[[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if vischeck[i][j]:
                continue
            currsize=0
            stackfornodestoexplore=[[i,j]]
            
            while len(stackfornodestoexplore):
                currnode=stackfornodestoexplore.pop()
                i=currnode[0]
                j=currnode[1]
                if vischeck[i][j]:
                    continue
                vischeck[i][j]=True
                if matrix[i][j]==0:
                    continue
                currsize+=1
                unvisitedneighbors=[]
                if i>0 and not vischeck[i-1][j]:
                    unvisitedneighbors.append([i-1,j])

                if i<len(matrix)-1 and not vischeck[i+1][j]:
                    unvisitedneighbors.append([i+1,j])    


                if j>0 and not vischeck[i][j-1]:
                    unvisitedneighbors.append([i,j-1])   



                if j<len(matrix[0])-1 and not vischeck[i][j+1]:
                    unvisitedneighbors.append([i,j+1])


                for neighbour in unvisitedneighbors:
                    stackfornodestoexplore.append(neighbour)

            if currsize>0:
                final.append(currsize)  
                    

    return final               



print(RiverSizes([[1,0,0,1,0],
                   [1,0,1,0,0],
                   [0,0,1,0,1],
                   [1,0,1,0,1],
                   [1,0,1,1,0]]))                     
     
    





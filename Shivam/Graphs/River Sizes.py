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
                ii=currnode[0]
                jj=currnode[1]
                
                if vischeck[ii][jj]:
                    continue
                vischeck[ii][jj]=True
                if matrix[ii][jj]==0:
                    continue
                currsize+=1
                unvisitedneighbors=[]
                if ii>0 and not vischeck[ii-1][jj]:
                    unvisitedneighbors.append([ii-1,jj])

                if ii<len(matrix)-1 and not vischeck[ii+1][jj]:
                    unvisitedneighbors.append([ii+1,jj])    


                if jj>0 and not vischeck[ii][jj-1]:
                    unvisitedneighbors.append([ii,jj-1])   



                if jj<len(matrix[0])-1 and not vischeck[ii][jj+1]:
                    unvisitedneighbors.append([ii,jj+1])


                for neighbour in unvisitedneighbors:
                    stackfornodestoexplore.append(neighbour)

            if currsize>0:
                final.append(currsize)  
                    

    return final               



print(RiverSizes([[1,0,1],
                  [0,1,0],
                  [1,0,1]]))                     
        
    





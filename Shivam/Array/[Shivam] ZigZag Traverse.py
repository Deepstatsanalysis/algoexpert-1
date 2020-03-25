def ZigZag(arr):
    colmax=len(arr[0])-1
    rowmax=len(arr)-1
    final=[]


    row=0
    col=0
    down=True

    while not ( col<0 or col > colmax or row <0 or row > rowmax ):
    
        final.append(arr[row][col])
        if down:
            if col==0 or row==rowmax:
                down=False
                if row==rowmax:
                    col+=1
                else:
                    row+=1


            else:
                row+=1
                col-=1



        else:
           
            if col==colmax or row==0:
                down=True
            
                if col==colmax: 
                    row+=1
                else:
                    col+=1


            else:
                row-=1
                col+=1



    return final





print(ZigZag([[1,3,4,10,11],
            [2,5,9,12,19],
            [6,8,13,18,20],
            [7,14,17,21,24],
            [15,16,22,23,25]]))
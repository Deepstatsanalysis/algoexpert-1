def waterarea(array):
    
    height=[0 for x in array]
    leftmax=0
    for i in range(len(array)):
        currheight=array[i]
    
        height[i]=leftmax
    
        leftmax=max(currheight,leftmax)
  
    rightmax=0
      
    for i in  reversed(range(len(array))):
        currheight=array[i]
        minheight=min(rightmax,height[i])
        if currheight< minheight:

            height[i]=minheight-currheight
        else:
            height[i]=0

        rightmax=max(rightmax,currheight)
      

    return sum(height)        



print(waterarea([0,8,0,0,5,0,0,10,0,0,1,1,0,3]))


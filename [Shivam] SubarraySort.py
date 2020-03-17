def SubarrySort(arr):
    currmin=float("inf")
    currmax=float("-inf")

    for i in range(0,len(arr)):
        num=arr[i]
        if i==0:
            if num > arr[i+1]:
                currmin= min(currmin,num)
                currmax= max( currmax,num)


        elif i>0 and i< len(arr)-1:
             if num > arr[i+1] or num < arr[i-1]:
                currmin=min( currmin,num)
                currmax=max( currmax,num)


        if i==len(arr)-1:
            if num < arr[i-1]:
                currmin=min( currmin,num)
                currmax=max( currmax,num)


    if  currmin ==float("inf"):
        return [-1,-1]         




    for j in range(0,len(arr)):
        if currmin <= arr[j]:
            min1=j
            break



    for k in range(len(arr)-1,-1,-1):
         if currmax >= arr[k]:
            max1=k
            print(arr[k],k)
            break




    return [min1,max1]


print(SubarrySort([1,2,4,7,10,11,7,12,6,7,16,18,19]))   


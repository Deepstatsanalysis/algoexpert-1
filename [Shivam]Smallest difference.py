def smalldif(arr1,arr2):
    arr1.sort()
    arr2.sort()
    l=0
    r=0
    final=[]
    smallest=float("inf")
    currdif=float("inf")
    while l<len(arr1) and r<len(arr2):
        first=arr1[l]
        second=arr2[r]
        if second==first:
            return [first,second]

        elif first<second:
            currdif=second-first
            if currdif<smallest:
                smallest=currdif
                final=[first,second]
            l+=1
            


        elif second<first:
            currdif=first-second
           
            if currdif<smallest:
                smallest=currdif
                final=[first,second]

            r+=1    


    return final    


print(smalldif([-1,5,10,20,28,3],[26,134,135,15,17]))  





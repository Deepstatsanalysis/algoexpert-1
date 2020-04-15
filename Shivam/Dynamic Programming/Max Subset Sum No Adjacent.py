def MaxSubsetSum(array):
    if not len(array):
        return
    elif len(array)==1:
        return array[0]

    second=array[0]        
    first=max(array[0],array[1])

    for i in range(2,len(array)):
        curr=max(first,second+array[i])
        second=first
        first=curr
    return first


print(MaxSubsetSum([7,10,12,7,9,14]))        

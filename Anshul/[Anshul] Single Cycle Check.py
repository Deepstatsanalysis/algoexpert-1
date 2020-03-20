list = [2,3,1,-4,-4,2]
list2 = [1,-1,1,-1]



def cyclecheck(arr):
    index = 0
    n = arr[index]

    for _ in range(len(arr)-1):
        index +=n
        n = arr[index]
        if index == 0:
            return False
    if index+n == 0 and arr[index+n]==arr[0]:
        return True
    else:
        False
    
print(cyclecheck(list))
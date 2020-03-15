 #sol1
def tnumsum(arr,target):
    nums={}
    for num in arr:
        x=target-num
        if x in nums:
            return [x,num]
        else:
            nums[num]=True
    return []            



print(tnumsum([3,5,-4,8,11,1,-1,6,5],50))



#sol2


def tnumsum2(arr,target):
    arr.sort()
    l=0
    r=len(arr)-1
    while l<r:
        if arr[l]+arr[r]==target:
           return [arr[l],arr[r]]
        elif arr[l]+arr[r]<target:
            l+=1
        elif arr[l]+arr[r]>target:      
             l-=1

    return []

print(tnumsum2([3,5,-4,8,11,1,-1,6,5],10))             



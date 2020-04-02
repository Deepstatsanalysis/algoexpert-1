arr1 = [10,15,8,12,94,81,5,2,11]
arr2 = [10,8,5,15,2,12,11,94,81]


# Solution 1   Space O(n*n)
def check(arr1,arr2):
    if len(arr1) != 0:
        print(arr1,arr2)
    if len(arr1) == 1 and len(arr2) == 1:
        if arr1[0] == arr2[0]:
            return True
             
    arr1list1=[]
    arr1list2=[]
    for i in range(1,len(arr1)):
        if arr1[i] < arr1[0]:
            arr1list1.append(arr1[i])
        if arr1[i] > arr1[0]:
            arr1list2.append(arr1[i])
    arr2list1=[]
    arr2list2=[]
    for i in range(1,len(arr2)):
        if arr2[i] < arr2[0]:
            arr2list1.append(arr2[i])
        if arr2[i] > arr2[0]:
            arr2list2.append(arr2[i])
    if len(arr1) != 0 and arr1[0] == arr2[0]:
        check(arr1list1,arr2list1)
        check(arr1list2,arr2list2)
        return True
    else:
        return False


print(check(arr1,arr2))



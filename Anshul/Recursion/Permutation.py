list = [1,2,3,4]

def helper(currentIndex, arr, perms):
    if currentIndex == len(arr)-1:
        perms.append(arr.copy())
    else:
        for j in range(currentIndex,len(arr)):
            arr[currentIndex],arr[j] = arr[j],arr[currentIndex]
            helper(currentIndex+1, arr, perms)
            arr[currentIndex],arr[j] = arr[j],arr[currentIndex]
    return perms

print(helper(0, list,[]))
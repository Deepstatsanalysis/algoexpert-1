# Solution : 1
arr = [4,7,9,4,2,8,7,10,14,25,32,12,7,3,5]
arr2 = [4,7,9,4,2,8,7,10,14,25,32,12,7,3,5]
arr3 = [4,7,9,4,2,8,7,10,14,25,32,12,7,3,5]

# Brute Force O(n*n)
def quickSort(arr):
    n=0
    m=0
    for j in range(len(arr)):
        for i in range(len(arr)-1):
            m += 1
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                n+=1
    return [arr,['Swaps',n],['Iterations',m]]

print(quickSort(arr))


# Solution : 2
def quickSort2(arr):
    n=0
    m=0
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(arr)-1):
            m+=1
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                n+=1
                isSorted = False
    return [arr,['Swaps',n],['Iterations',m]]

print(quickSort2(arr2))


# Solution : 3
def quickSort3(arr):
    n=0
    m=0
    count = 0
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(arr)-1-count):
            m+=1
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                n+=1
                isSorted = False
        count+=1
    return [arr,['Swaps',n],['Iterations',m]]

print(quickSort3(arr3))
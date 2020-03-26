list1 = [8,5,2,9,5,6,3]

def insertionSort(arr):
    for i in range(1,len(arr)):
        j = i
        while arr[j]<arr[j-1] and j > 0:
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j = j-1
    return arr



print(insertionSort(list1))
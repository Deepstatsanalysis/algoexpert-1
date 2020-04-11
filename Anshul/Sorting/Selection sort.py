list = [8, 5, 2, 9, 5, 6, 3]

def selectionSort(arr):
    i=0
    while i<len(arr):
        smallestIndex = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[smallestIndex]:
                smallestIndex = j
        arr[smallestIndex],arr[i] = arr[i], arr[smallestIndex]
        print(arr)
        i+=1


    return arr

print(selectionSort(list))
import heapq
listEx = [8, 5, 2, 9, 5, 6,3]



# Via min Heap
def heapSort(arr):
    temp = []
    while len(arr) > 0:
        heapq.heapify(arr)
        temp.append(heapq.heappop(arr))
    return temp

print(heapSort(listEx))


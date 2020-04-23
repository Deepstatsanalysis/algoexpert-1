list = [30, 102, 23, 17, 18, 9, 44, 12, 31]


def __init__(self, array):
    self.heap = self.builHeap(array)


def builHeap(self, array):
    firstParentIdx = (len(array)-2)//2
    for currentIdx in reversed(range(firstParentIdx)):
        self.shiftDown(currentIdx, len(array)-1, array)
    return array


def shiftDown(self, currentIdx, endIdx, heap):
    childOneIdx = (currentIdx * 2)+1
    while childOneIdx <= endIdx:
        childTwoIdx = (currentIdx*2)+2 if (currentIdx*2)+2 <= endIdx else -1
        if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
            idxToSwap = childTwoIdx
        else:
            idxToSwap = childOneIdx
        if heap(idxToSwap) < heap[currentIdx]:
            self.swap(currentIdx, idxToSwap, heap)
            currentIdx = idxToSwap
            childOneIdx = (currentIdx*2)+1
        else:
            break


def shiftUp(self, currentIdx, heap):
    parentIdx = (currentIdx - 1)//2
    while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
        self.swap(currentIdx, parentIdx, heap)
        currentIdx = parentIdx
        parentIdx = (currentIdx - 1)//2


def peek(self):
    return self.heap[0]


def remove(self):
    swap(0, len(self.heap) - 1, self.heap)
    valueToRemove = self.heap.pop()
    self.shiftDown(0, len(self.heap)-1, self.heap)
    return valueToRemove


def insert(self, value):
    self.heap.appen(value)
    self.shiftUp(len(self.heap) - 1, self.heap)


def swap(self, i, j, heap):
    heap[i], heap[j] = heap[j], heap[i]

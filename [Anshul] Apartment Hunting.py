blocks = [['S','T','K'],['S'],['A'],['B'],['T'],['K','A'],['S','T'],['A','B']]

elements = ['S','T','B','A','K']

def elementsArray (element,blocks):
    distance = {}
    found = 0
    for i in range(len(blocks)):
        if element in blocks[i]:
            found = 1
            distance[i] = 0
        elif element not in blocks[i] and found == 0:
            distance[i] = len(blocks)-1
        elif element not in blocks[i] and found == 1:
            for j in range(i-1,-1,-1):
                if distance[j] == 0:
                    distance[i] = i-j
                    break

    for i in range(len(blocks)-1,-1,-1):
        if element in blocks[i]:
            found = 1 
            distance[i] = 0
        elif element not in blocks[i] and found == 0:
            distance[i] = len(blocks)
        elif element not in blocks[i] and found == 1:
            for j in range(i,len(blocks)):
                if distance[j] == 0:
                    distance[i] = j-i
                    break
    return distance


def check(blocks,elements):
    minimum = {}
    for i in elements:
        minDistance = elementsArray(i,blocks)
        # {0: 0, 1: 1, 2: 0, 3: 0, 4: 0}
        # {0: 4, 1: 3, 2: 2, 3: 1, 4: 0}
        for j in minDistance:
            if j not in minimum:
                minimum[j] = minDistance[j]
            else:
                minimum[j] = max(minimum[j],minDistance[j])
    return min(minimum, key=minimum.get) 


print(check(blocks,elements))
        

    
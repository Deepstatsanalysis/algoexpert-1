list = [1,11,3,0,15,5,2,4,10,7,12,6]


def range(arr):
    d = {}
    for i in arr:
        d[i] = True
    range1 = []
    length = 0

    for i in arr:
        if not d[i]:
            continue
        d[i] = False
        currentLength = 1
        left = i-1
        right = i+1
        while left in d:
             d[left] = False
             currentLength +=1
             left -=1
        while right in d:
            d[right] = False
            currentLength +=1
            right +=1
        if currentLength > length:
            length = currentLength
            range1 = [left+1, right-1]
    return [range1,length]
        
        

print(range(list))
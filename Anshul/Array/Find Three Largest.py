list = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

def threeLargest(arr):
    count = [None, None, None]
    for i in range(len(arr)-1):
        if count[2] is None or arr[i] > count[2]: update(count, arr[i], 2)
        elif count[1] is None or arr[i] > count[1]: update(count, arr[i], 1)
        elif count[0] is None or arr[i] > count[0]: update(count, arr[i], 0)
    return count

def update(count, num, idx):
    for i in range(idx + 1):
        if i == idx: count[i] = num
        else: count[i] = count[i+1]

print(threeLargest(list))
eg = [7, 10, 12, 7, 9, 14, 5, 34, 12, 19, 55, 56]

def mssna(arr):
    temp = [0,0]
    ans = 0
    for i in range(len(arr)):
        ans = max(temp[1],temp[0]+arr[i])
        temp[0] = temp[1]
        temp[1] = ans

    return temp[1]


print(mssna(eg))
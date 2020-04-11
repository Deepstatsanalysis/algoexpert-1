coins = [1,5,10,25]

def changeWays(arr, value):
    ways = {}
    for i in range(value+1):
        ways[i]=0
    ways[0]=1
    for i in range(len(arr)):
        for j in ways:
            if arr[i] <= j and j!=0:
                ways[j] += ways[j-arr[i]]
        print(ways)
        
    return ways


print(changeWays(coins, 5))

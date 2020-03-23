list = [8,4,2,1,3,6,7,9,5]



def solve(list):
    d = [1 for j in range(len(list))]

    for i in range(1,len(list)):
        if list[i] > list[i-1]:
            d[i] = d[i-1]+1
    for i in range(len(list)-2,-1,-1):
        if list[i-1] > list[i]:
            d[i-1] = max(d[i-1], d[i]+1)
    return d
        
print(solve(list))

# O(n) Time || O(n) Space
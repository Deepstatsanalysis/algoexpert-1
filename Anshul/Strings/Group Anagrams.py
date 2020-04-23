example = ['yo','flop', 'act', 'olfp', 'tac','oy', 'cat']

 
# Space : O(WN) || Time : O(WNlog(N))

def solve(arr):
    d={}
    for i in range(len(arr)):  #W
        temp = ''.join(sorted(arr[i])) #Nlog(N)
        if temp not in d:
            d[temp] = [i] 
        else: 
            d[temp].append(i)
    ans = []
    for i in d:
        temp=[]
        for j in d[i]:
            temp.append(arr[j])
        ans.append(temp)

    return ans
print(solve(example))
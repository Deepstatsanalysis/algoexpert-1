import itertools
n = int(input())
testCase = []
for i in range(n):
    testCase.append(list(map(int,input().split())))


def bracket(n,k,m):  # 3 ,6
    ans = ''
    def matrix(n):
        matrix = []
        fm = []
        for i in range(1,n+1):
            fm.append(i)
        for j in range(len(fm)):
            matrix.append(fm[j:]+fm[:j-len(fm)])
        return matrix

    matrix1 = matrix(n)
    output = list(itertools.permutations(matrix1))
    def diagonal(matrix):
        value = 0
        for i in range(len(matrix)):
            value += matrix[i][i]
        return value
        
    for i in output:
        temp = diagonal(list(i))
        if temp == k: 
            ans = 'POSSIBLE'
            matrix1 = list(i)
            break
        
    if ans == 'POSSIBLE':
        print('Case #'+str(m+1)+': POSSIBLE')
        for i in range(len(matrix1)):
            ans = ''
            for j in range(len(matrix1)):
                ans+=str(matrix1[i][j])+' '
            if i != len(matrix1)-1: print(ans[:-1])
        return ans[:-1]
    else:
        return 'Case #'+str(m+1)+': IMPOSSIBLE'


for i,e in enumerate (testCase):
    print(bracket(testCase[i][0],testCase[i][1],i))






 def search(self, nums: List[int], target: int) -> int:
        def h(l,r):
            if l > r:
                return -1
            m = (r+l)//2
            if nums[m] == target:
                return m
            
            if nums[l] <= target < nums[m] or (nums[m] <= nums[r]  and not nums[m] < target <= nums[r]):
                return h(l,m-1)
            else: 
                return h(m+1, r)
        return h(0,len(nums)-1)
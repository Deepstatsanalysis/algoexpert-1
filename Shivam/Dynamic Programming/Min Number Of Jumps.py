def minjumps(array):
    jumps=[float("inf") for x in array]
    jumps[0]=0
    for i in range(1,len(array)):
        for j in range(0,i):
            if array[j] + j>=i:
                jumps[i]=min(jumps[j]+1,jumps[i])

    return jumps[-1]



#sol 2
def minj(array):
    if len(array) ==1:
        return 0
    jumps=0
    maxreach=array[0]
    steps=array[0]
    for i in range (1,len(array)-1):
        maxreach=max(maxreach,i + array[i])
        steps-=1
        if steps == 0:
            jumps+=1
            steps= maxreach-i
            print(maxreach,i)
            print(steps)
    return jumps+1



print(minjumps([3,5,5,1,2,3,7,1,1,1,3]))   
print(minj([3,5,5,1,2,3,7,1,1,1,3]))    
          # 0 1 2 3 4 5 6 7 8 9 10                         
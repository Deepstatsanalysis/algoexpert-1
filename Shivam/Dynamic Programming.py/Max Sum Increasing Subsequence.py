def maxincsub(array):
    sub=[None for i in array]
    sums=array[:]
    maxind=0
    for i in range(0,len(array)):
        curr=array[i]
        for j in range(0,i):
            num2=array[j]
            if num2<curr and sums[j]+curr >=sums[i]:
                sums[i]=sums[j]+curr
                sub[i]=j
        if sums[i]>=sums[maxind]:
            maxind=i

    return [sums[maxind],sequence(array,sub,maxind)]



def sequence(array,sub,maxind):
    seqarray=[]
    while maxind is not None:
        seqarray.append(array[maxind])
        maxind=sub[maxind]

    return list(reversed(seqarray))  


print(maxincsub([8,12,2,3,15,5,7]))                             
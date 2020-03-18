def FourNumSUm(arr,value):
    final=[]
    hashset={}
    for i in range(1,len(arr)-1):
        for j in range(i+1,len(arr)):   
            p=arr[i] + arr[j] 
            diff=value-p
            if diff in hashset:
                for pair in hashset[diff]:
                    final.append(pair + [arr[i],arr[j]])


        for k in range(0,i):                     
            q=arr[k]+arr[i]
            if q not in hashset:
                hashset[q]=[[arr[i],arr[k]]]
            else:
                hashset[q].append([arr[i],arr[k]])


    return final                            

# [[6,7,4,-1],[7,6,1,2]]


#print(FourNumSUm([10,20,30,40,1,2],91))
print(FourNumSUm([7,6,4,-1,1,2],16))




def fourNumberSum(array, targetSum):
    allPairSums = {}
    quadruplets = []
    for i in range(1, len(array) - 1):
        for j in  range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in allPairSums:
                for pair in allPairSums[difference]:
                    quadruplets.append(pair + [array[i], array[j]])
        for k in range(0, i):
            currentSum = array[i] +  array[k]
            if currentSum not in allPairSums:
                allPairSums[currentSum] = [[array[k], array[i]]]
            else:
                allPairSums[currentSum].append([array[k], array[i]])
    return quadruplets



input = [7,  6, 4, -1, 1, 2]
output = fourNumberSum(input, 16)
print('Quadruplets: ', output)
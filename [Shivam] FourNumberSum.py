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
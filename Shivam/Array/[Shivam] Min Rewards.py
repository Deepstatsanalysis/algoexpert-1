#Sol
def MinRewards(arr):
    final=[]
    minlist=[]
    for i in range(0,len(arr)):
        final.append(1)
    
    

     
    if len(arr)==1:
         minlist.append(0)


    else:



        for j in range(0,len(arr)-1):

            if j==0 and  arr[j]< arr[j+1]:
                minlist.append(j)



            if j==len(arr)-1 and  arr[j]< arr[j-1]:
                minlist.append(j)     

   





            if arr[j]<arr[j-1] and arr[j]<arr[j+1]:
                    minlist.append(j)
    



    for mins in minlist:

        left=mins-1
        while left >=0:
            if arr[left]< arr[left+1]:
                break

            else:
                final[left]=max(final[left],final[left+1]+1)
                
                left-=1



        right =mins+1
        while right< len(arr)-1:
            if arr[right]<final[right-1]:
                break


            else:
                 final[right]=final[right-1]+1
                 right+=1


   

    return sum(final)






print(MinRewards([8,4,2,1,3,6,7,9,5]))


#Sol2

def Sol2(arr):
    final1=[]
    for i in range(0,len(arr)):
        final1.append(1)
    
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            final1[i]=final1[i-1]+1



    for j in range(len(arr)-2,-1,-1):
        if arr[j]>arr[j+1]:
            final1[j]=max(final1[j],final1[j+1]+1)   


 

    return sum(final1)

    
print(Sol2([8,4,2,1,3,6,7,9,5]))                 

        


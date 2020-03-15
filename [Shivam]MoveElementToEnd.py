def moveend(arr,tar):
    i=0
    j=len(arr)-1

    while i<j:
        if arr[i]==tar and arr[j]!=tar:
            arr[i],arr[j]=arr[j],arr[i]
            
            j-=1
            i+=1
            
            continue

        elif arr[i]!=tar and arr[j]==tar:
            
            j-=1
        


        elif arr[i]==tar and arr[j]==tar:  
        
            j-=1
        
            continue


        elif arr[i]!=tar and arr[j]!=tar:   
            
            i+=1
            
            continue

      

    return arr

print(moveend([2,1,2,2,3,4,2],2))          
           



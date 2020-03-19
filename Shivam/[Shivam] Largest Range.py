def LargestRange(arr):
    hashset={}
    final=[]
    largestrange=0
  

    for num in  arr:
        hashset[num]=True


    for num in  arr:
        if  not hashset[num]:
            continue    

        else:
            hashset[num]=False
            leftrange=num-1
            rightrange=num+1
            currentrange=1


            while leftrange in hashset:
                hashset[leftrange]=False

                leftrange-=1
                currentrange+=1




            while rightrange in hashset:
                hashset[rightrange]=False
                rightrange+=1
                currentrange+=1




            if currentrange>largestrange:
                largestrange=currentrange   
                final=[leftrange+1,rightrange-1]

    


    return final




print(LargestRange([1,11,3,0,15,5,2,4,10,7,12,6]))
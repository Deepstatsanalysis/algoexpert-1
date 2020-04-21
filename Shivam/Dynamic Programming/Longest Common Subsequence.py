def lcs(str1,str2):
    array=[[[None,0,None,None]for x in range(len(str1)+1)]for y in range(len(str2)+1)]
    for i in range(1,len(str2)+1):
        for j in range(1,len(str1)+1):
            if str2[i-1]==str1[j-1]:
                array[i][j]=[str2[i-1],array[i-1][j-1][1]+1,i-1,j-1]

            else:
                if array[i][j-1][1] > array[i-1][j][1]:
                    array[i][j]=[None,array[i][j-1][1],i,j-1]
                else:
                    array[i][j]=[None,array[i-1][j][1],i-1,j]
                   

    return sequence(array)


def sequence(array):
    seq=[]
    i=len(array)-1
    j=len(array[0])-1
    while i!=0 and j!=0:
        curr=array[i][j]
        if curr[0] is not None:
            seq.append(curr[0])

        i=curr[2]
        j=curr[3]
          

    return list(reversed(seq)) 



print(lcs('xkykzpw','zxvvyzw'))           





                
                   

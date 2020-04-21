def lps(string):
    curr=[0,1]
    for i in range(1,len(string)):
        odd=getlongest(string,i-1,i+1)
        even=getlongest(string,i-1,i)
        longest=max(odd,even,key=lambda x:x[1]-x[0])
        curr=max(longest,curr,key=lambda x:x[1]-x[0])

    return string[curr[0]:curr[1]]

def getlongest(string,left,right):
    while left >=0 and right < len(string):
        if string[left] !=string[right]:
            break
        left-=1
        right+=1
    return [left+1,right]    


print(lps('abaxyzqzyxf'))    
def ispalindrome(string,i=0):
    j=len(string)-1-i
    if i>=j:
        return True

    if string[i]!=string[j]:
        return False

    return ispalindrome(string,i+1)        

print(ispalindrome('abcdjdcba'))
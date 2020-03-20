string = 'abcdjdcba'

# 1st Solution

def check(string):
    string2 = string[::-1]
    if string == string2:
        return True
    else:
        return False



# 2nd Solution

def check2(string):
    initial = 0
    final = len(string)-1
    while initial < final:
        if string[initial] == string[final]:
            initial+=1
            final -=1 
        else:
            return False
    return True
    
print(check2(string))
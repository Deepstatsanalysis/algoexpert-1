string = 'xyzahyjfg'

def cce(string, key):
    arr = []
    for i in range(len(string)):
        arr.append(solve(string, i, key))
    return "".join(arr)

def solve(string, idx, key):
    value = ord(string[idx])+key%26
    if value <= 122:return chr(value)
    else : return chr(96+value%122)



print(cce(string, 4))
print(cce(string, 30))
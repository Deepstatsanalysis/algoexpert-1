
# My Solution
sample = 'clemyentisacap'
def find(string):
    dict = {}
    ans = ''
    result = ''
    i=0
    while i<len(string):
        if string[i] not in dict:
            dict[string[i]] = int(i)
            i+=1
        else:
            ans = ''.join(list(dict.keys()))
            if len(result)<len(ans):
                result = ans
            i = dict[str(string[i])]+1
            dict={}
    return result

print(find(sample))




#Efficient one

def lengthOfLongestSubstring(s):
    lastSeen = {}
    longest = [0, 1]
    startIndex = 0
    for i, char in enumerate(s):
        if char in lastSeen:
            startIndex = max(startIndex, lastSeen[char] + 1)
        if longest[1] - longest[0] < i + 1 - startIndex:
            longest = [startIndex, i + 1]
        lastSeen[char] = i
    return s[longest[0]:longest[1]]
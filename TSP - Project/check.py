
def standard_input():
    yield 2
    yield '4 4'
    yield '6 9'

t = int(input())
for i in range(1, t + 1):
    n, m = [int(s) for s in input().split(" ")]
    print("Case #{}: {} {}".format(i, n + m, n * m))
    
    

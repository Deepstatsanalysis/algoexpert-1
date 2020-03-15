def fib(n):
    k=[0,1]
    for i in range(n-1):
        k[0],k[1] = k[1],k[0]
        k[1] += k[0]
    return k[1] if n > 1 else k[0]


print(fib(10))


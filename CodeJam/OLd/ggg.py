def printf(*args, **kwargs): print(*args, **kwargs, flush=True)


t = int(input())
for ti in range(1, t + 1):
    r, s = map(int, input().split())
    printf("Case #{}: {}".format(ti, (r * (s - 1) + 1) // 2))
    if r % 2:
        p = r + 1
        for i in range(1, s):
            for j in range(0, r - 1, 2):
                printf(2 * i, p - 2 * i)
                p += 2
            if i % 2:
                if i == s - 1:
                    printf(i, p - i)
                else:
                    printf(2 * i + 1, p - 2 * i - 1)
                    p += 2
    else:
        p = r + 1
        for i in range(1, s):
            for j in range(0, r, 2):
                printf(2 * i, p - 2 * i)
                p += 2

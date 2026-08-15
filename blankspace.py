t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    current = 0
    maximum = 0

    for x in a:
        if x == 0:
            current += 1
            maximum = max(maximum, current)
        else:
            current = 0

    print(maximum)
t = int(input())

for _ in range(t):
    n = int(input())

    # Minimum time for each skill combination
    best = {
        "00": float('inf'),
        "01": float('inf'),
        "10": float('inf'),
        "11": float('inf')
    }

    for _ in range(n):
        m, s = input().split()
        m = int(m)

        best[s] = min(best[s], m)

    # Option 1: one book that gives both skills
    answer = best["11"]

    # Option 2: one book for skill 1 + one book for skill 2
    answer = min(answer, best["10"] + best["01"])

    if answer == float('inf'):
        print(-1)
    else:
        print(answer)
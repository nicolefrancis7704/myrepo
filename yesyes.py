t = int(input())

pattern = "Yes"

for _ in range(t):
    s = input()

    possible = False

    for start in range(3):
        if all(s[i] == pattern[(start + i) % 3] for i in range(len(s))):
            possible = True
            break

    print("YES" if possible else "NO")
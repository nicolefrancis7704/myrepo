s = input()

current = 'a'
answer = 0

for ch in s:
    distance = abs(ord(ch) - ord(current))

    # Because the alphabet is circular
    answer += min(distance, 26 - distance)

    current = ch

print(answer)
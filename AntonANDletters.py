s = input()

letters = set()

for ch in s:
    if ch.islower():
        letters.add(ch)

print(len(letters))
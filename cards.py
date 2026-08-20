n = int(input("#Cards: "))
cards = list(map(int, input("Cards: ").split()))

sereja = 0
dima = 0

left = 0
right = n - 1

for i in range(n):

    if cards[left] > cards[right]:
        maximum = cards[left]
        left += 1
    else:
        maximum = cards[right]
        right -= 1

    if i % 2 == 0:
        sereja += maximum
    else:
        dima += maximum

print(sereja, dima)



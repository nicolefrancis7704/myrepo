keyboard="qwertyuiopasdfghjkl;zxcvbnm,./"
direction=input("Enter direction:")
inp=input("Enter message:")
res=""

for i in inp :
    pos=keyboard.index(i)
    if direction == 'R' :
        res+=keyboard[pos -1]
    else :
        res+=keyboard[pos+1]

print(res)


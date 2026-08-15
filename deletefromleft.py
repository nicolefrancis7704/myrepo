s=input()
t=input()

i=len(s)-1
j=len(t)-1

common=0 

while i >= 0 and j >=0 and s[i]==t[j] :
    common+=1
    i-=1
    j-=1

print(len(s)+len(t)-2*common)
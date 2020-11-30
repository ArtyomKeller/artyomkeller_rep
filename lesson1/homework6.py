a = int(input())
b = int(input())
y = 0
while a < b:
    a += (a/100)*10
    y+=1
    continue
print(y+1)

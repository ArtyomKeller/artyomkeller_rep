a = int(input())
b = int(input())
z = 0
while a < b:
    a += (a/100)*10
    z+=1
    continue
print(z+1)

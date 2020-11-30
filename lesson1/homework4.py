i = int(input())
z = 0
if i >= 10:
    while i > 10:
        d = i % 10
        i //= 10
        if d > z:
            z = d
    print(z)
else:
    print(i)
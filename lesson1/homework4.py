i = int(input())
m = 0
if i >= 10:
    while i > 10:
        d = i % 10
        i //= 10
        if d > m:
            m = d
    print(m)
else:
    print(i)
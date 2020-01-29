a,b,c = [int(x) for x in input().split()]

print(a) if a>b and a>c else print(b) if b>c else print(c)
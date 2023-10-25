a = int(input())
b = int(input())
c = int(input())

m = 0

if a > b:
    m = a
else:
    m = b

if c > m:
    print(c)
else:
    print(m)

# print(max(a, b, c))
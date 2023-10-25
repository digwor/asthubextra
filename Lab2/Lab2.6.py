a = int(input())
b = int(input())
c = int(input())

srednee = abs((max(a, b, c) + min(a, b, c)) - (a + b + c))
print(min(a, b, c), srednee, max(a, b, c))
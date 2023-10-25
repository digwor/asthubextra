a = int(input())
b = int(input())
if a > 1000 or b > 1000:
    print('Введите числa меньше 1000')
else:
    hyp = (a ** 2 + b ** 2) ** 0.5
    print(hyp)
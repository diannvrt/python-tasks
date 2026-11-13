#Дан список A из N чисел. Вывести сумму элементов и произведение элементов с чётными индексами (0, 2, 4...)
n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

summary = 0
product = 1

for i in range(0, len(a), 2):
    summary += a[i]
    product *= a[i]
    
print(summary)
print(product)
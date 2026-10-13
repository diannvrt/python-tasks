#Дан список A из N чисел. Генератором вывести элементы, большие среднего, и само среднее
n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

avg = sum(a) / len(a)
above = [x for x in a if x > avg]

print(above)
print(avg)
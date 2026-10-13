#Дан список A из N чисел. Вывести элементы, большие среднего арифметического всех элементов, и их количество
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

total = 0
for x in a:
    total += x
    
average = total / n

count = 0
for x in a:
    if x > average:
        print(x)
        count += 1
print(count)
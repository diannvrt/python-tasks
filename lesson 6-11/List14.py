#Дан список A из N чисел и число D. Вывести число вхождений D (count) и индекс первого вхождения (или -1, если D нет)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

d = int(input())
count = a.count(d)
if d in a:
    idx = a.index(d)
else:
    idx = -1
    
print(count)
print(idx)

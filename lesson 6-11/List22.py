#Дан список A из N чисел и число D. Генератором вывести элементы, умноженные на D, и количество элементов, равных D
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

d = int(input())
pr = [x * d for x in a ]
equal = [x for x in a if x == d]

print(pr)
print(len(equal))
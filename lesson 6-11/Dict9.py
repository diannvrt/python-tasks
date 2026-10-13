#Построить словари из N и M пар. Слить второй в первый через update. Вывести размер
# результата и значение ключа, который был в обоих словарях (такой ключ гарантированно есть)
n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

m = int(input())
b = {}
for i in range(m):
    key = input()
    value = int(input())
    b[key] = value

c = None
for key in b:
    if key in d:
        c = key
        break

d.update(b)
print(len(d))
print(d[c])
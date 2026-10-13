#Построить словари из N и M пар. Добавить в первый пары второго без update: только ключи,
#которых нет; совпавшие ключи считать проигнорированными. Вывести размер и число проигнорированных
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
    
ignored = 0
for key in b:
    if key in d:
        ignored += 1
    else:
        d[key] = b[key]

print(len(d))
print(ignored)
#Дан список из N строк. Генератором вывести список длин строк и суммарную длину всех строк
n = int(input())
a = []
for i in range(n):
    a.append(input())
    
l = [len(x) for x in a]
s = sum(l)

print(l)
print(s)

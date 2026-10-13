#Дан список из N строк и буква. Генератором вывести строки, начинающиеся с этой буквы (первый символ строки)
n = int(input())
a = []
for i in range(n):
    a.append(input())

s = input()
st = [x for x in a if x[0] == s]

print(st)

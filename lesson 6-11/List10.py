#Дан список из N строк. Вывести самую длинную и самую короткую строку (первую из встретившихся) и их длины
n = int(input())
a = []

for i in range(n):
    a.append(input())

longest = 0
shortest = 0

for s in a:
    if len(s) > len(longest):
        longest = s
    if len(s) < len(shortest):
        shortest = s

print(longest, len(longest))
print(shortest, len(shortest))
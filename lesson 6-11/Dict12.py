#Построить словарь из N пар с различными значениями. Построить обращённый словарь: значение ключ.
# Вывести его пары в порядке добавления исходного
N = int(input())
d = {}
for i in range(N):
    key = input()
    value = int(input())
    d[key] = value


n = {} 
for key, value in d.items():
    n[value] = key
for value in n:
    print(f'{value}: {n[value]}')
    
    
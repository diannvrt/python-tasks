#Построить словарь из N троек: название, цена, количество (значение — список из двух чисел).
#Вывести суммарную стоимость склада и название самого дорогого по стоимости предмета
n = int(input())
d = {}
for i in range(n):
    key = input()
    price = int(input())
    qty = int(input())
    d[key] = [price, qty]

total = 0
best = None
best_cost = 0

for key in d:
    price, qty = d[key]
    cost = price * qty
    total += cost
    if cost > best_cost:
        best = key
        best_cost = cost
        
print(total)
print(best)
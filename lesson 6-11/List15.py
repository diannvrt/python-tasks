#Дан список A из N чисел. Вывести элементы на нечётных позициях (1, 3, 5... при счёте позиций с 1) и их сумму

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
odd_positions = a[::2]
total = (sum(odd_positions))
print(odd_positions)
print(total)
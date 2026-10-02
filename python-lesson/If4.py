#Даны три целых числа. Найти количество положительных чисел в исходном наборе.
count = 0

a = int(input())
b = int(input())
c = int(input())
if a > 0:
    count += 1
if b > 0:
    count += 1
if c > 0: 
    count += 1
print(count)
#Даны три целых числа. Найти количество положительных и количество
# отрицательных чисел в исходном наборе.

a = int(input())
b = int(input())
c = int(input())
count_pos = 0
count_neg = 0

if a > 0:
    count_pos += 1
elif a < 0:
    count_neg += 1

if b > 0:
    count_pos += 1
elif b < 0:
    count_neg += 1

if c > 0:
    count_pos += 1
elif c < 0:
    count_neg += 1

print(count_pos)
print(count_neg)
    
    
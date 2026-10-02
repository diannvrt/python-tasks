#Даны два целых числа A и B (A < B). Найти сумму квадратов всех целых чисел от A до B включительно.
A = int(input())
B = int(input())
total = 0
for i in range(A, B + 1):
    total += i ** 2
print(total)
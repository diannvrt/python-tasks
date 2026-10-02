#Даны два целых числа A и B (A < B). Найти произведение всех целых чисел от A до B включительно.

product = 1
A = int(input())
B = int(input())
for i in range(A, B + 1):
    product *= i
print(product)
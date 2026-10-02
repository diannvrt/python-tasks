#Даны три целых числа: A, B, C. Проверить истинность высказывания: «Ровно два из чисел A, B, C являются положительными».
A = int(input())
B = int(input())
C = int(input())
print(
    (A > 0 and B > 0 and C <= 0) or
    (B > 0 and C > 0 and A <= 0) or 
    (A > 0 and C > 0 and B <= 0)
)
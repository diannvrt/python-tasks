#Даны чётное N (> 0) и символы C1, C2. Вывести строку длины N из чередующихся C1 и C2, начиная с C1
N = int(input())
C1 = input()
C2 = input()

s = ''.join(C1 if i % 2 == 0 else C2 for i in range(N))
print(s)
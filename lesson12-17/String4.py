#Дано N (1 ≤ N ≤ 26). Вывести строку из N первых заглавных латинских букв
N = int(input())
s = ''
for i in range(N):
    s += chr(ord('A') + i)
print(s)
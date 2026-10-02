#Дано целое число N (> 0). Найти произведение 1.1 · 1.2 · 1.3 · ... (N сомножителей).
N = int(input())
product = 1

for i in range(1, N + 1):
    product *= (10 + i) / 10
print(product)
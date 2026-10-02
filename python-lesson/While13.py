#Дано число A (> 1). Вывести наименьшее из целых чисел K, для которых сумма 1 + 1/2 + ... + 1/K
# будет больше A, и саму эту сумму.
A = float(input())
K = 0
total = 0.0
while total <= A:
    K += 1
    total += 1 / K
print(K)
print(total)

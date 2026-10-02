#Даны переменные A, B, C. Изменить их значения, переместив содержимое A в C,
# C — в B, B — в A, и вывести новые значения переменных A, B, C.
A = int(input('Введите A: '))
B = int(input('Введите B: '))
C = int(input('Введите C: '))
temp = A
A = B
B = C
C = temp
print(f'A: {A}')
print(f'B: {B}')
print(f'C: {C}')
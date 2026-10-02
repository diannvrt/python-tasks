#Даны два ненулевых числа. Найти сумму, разность, произведение и частное их модулей.

a = float(input('Введите a: '))
b = float(input('Введите b: '))

abs_a = abs(a)
abs_b = abs(b)

total = abs_a + abs_b
diff = abs_a - abs_b
product = abs_a * abs_b
quotient = abs_a / abs_b

print(f'Сумма модулей: {total}')
print(f'Разность модулей: {diff}')
print(f'Произведение модулей: {product}')
print(f'Частное модулей: {quotient}')
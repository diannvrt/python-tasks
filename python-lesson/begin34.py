#Известно, что X кг шоколадных конфет стоит A рублей, а Y кг ирисок стоит B рублей. 
# Определить, сколько стоит 1 кг шоколадных конфет, 1 кг ирисок, а также во сколько раз шоколадные конфеты дороже ирисок.
X = float(input())
A = float(input())
Y = float(input())
B = float(input())
price_x = A
price_x1kg = A / X

price_y = B
price_y1kg = B / Y

difference = price_x1kg / price_y1kg

print(f'Стоимость 1 кг шоколадных конфет: {price_x1kg}')
print(f'Стоимоcть 1 кг ирисок: {price_y1kg}')
print(f'Разница в стоимости: {difference}')
#Известно, что X кг конфет стоит A рублей. Определить, сколько стоит 1 кг и Y кг этих же конфет.
X = float(input())
A = float(input())
Y = float(input())
price_xkg = A / X
price_ykg = price_xkg * Y
print(f'Цена за 1 кг: {price_xkg}')
print(f'Цена за Y кг: {price_ykg}')

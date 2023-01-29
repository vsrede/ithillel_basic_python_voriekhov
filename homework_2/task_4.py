from decimal import Decimal
value_uah = int(input('Введіть кількість гривень '))
kurs_exchange = Decimal(8)
print('Станом на 25 серпня 2022 року це становить', Decimal(value_uah) / Decimal(kurs_exchange), 'Долари США :(') 



products = ['Молоко', 'Яблоко', 'Шоколад', 'Сыр', 'Ряженка', 'Груша']
count = len(products)

for product in products:
    if len(product) % 2 == 0:
        print(product)
sales = float(input('Введите значение выручки: '))
costs = float(input('Введите значение издержек: '))
if sales > costs:
    profit = (sales - costs) / sales * 100
    print(f'Ваша фирма работает с прибылью. Рентабельность выручки составила {profit:.2f}%')
    workers = int(input('Введите количество работников: '))
    print(f'Рентабельность выручки на каждого работника составила {profit / workers:.2f}%')
elif costs > sales:
    print('Ваша фирма работает с убытком')
else:
    print('Ваша фирма работает с нулевой прибылью/убытком')

a = int(input("Результат спортсмена в первый день (км): "))
b = int(input("Желаемый результат (км): "))
result_days = 1
result_km = a
while result_km < b:
        a = a * 1.1
        result_days += 1
        result_km = result_km + a
print(f'Общий результат спортсмена составит не менее {b} километров на {result_days} день')

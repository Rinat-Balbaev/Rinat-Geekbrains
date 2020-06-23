from sys import argv

name, time, salary, bonus = argv[1:]
try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    total = time * salary + bonus
    print(f'Заработная плата сотрудника {total}')
except ValueError:
    print('Некорректный формат данных')
def my_sum ():
    total = 0
    end_input = False
    while end_input == False:
        number = input('Input numbers with space in between or press Q for quit: ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                end_input = True
                break
            else:
                res = res + int(number[el])
        total = total + res
        print(f'Current sum is {total}')
    print(f'Your total sum is {total}')


my_sum()
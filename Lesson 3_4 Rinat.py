def my_func(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    return 1 / res

print(my_func(float(input('Enter positive integer: ')), abs(int(input('Enter negative power(integer): '))) * (-1)))

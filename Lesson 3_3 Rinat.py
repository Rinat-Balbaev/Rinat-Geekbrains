arg1 = int(input('Enter arg1: '))
arg2 = int(input('Enter arg2: '))
arg3 = int(input('Enter arg3: '))

def my_func(arg1, arg2, arg3):
    args_list = [arg1, arg2, arg3]
    result = []
    max1 = max(args_list)
    result.append(max1)
    args_list.remove(max1)
    max2 = max(args_list)
    result.append(max2)
    print(sum(result))

my_func(arg1, arg2, arg3)
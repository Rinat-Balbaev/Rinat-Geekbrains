with open('test_3.txt', 'r') as my_file:
    sal = []
    less20 = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           less20.append(i[0])
        sal.append(i[1])
print(f'{less20} have salary less than 20000. Average salary is {sum(map(int, sal)) / len(sal)}')
def my_sum():
    try:
        with open('test_5.txt', 'w+') as file_obj:
            line = input('Enter numbers with Space in between \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('IOError')
    except ValueError:
        print('Incorrect value')
my_sum()
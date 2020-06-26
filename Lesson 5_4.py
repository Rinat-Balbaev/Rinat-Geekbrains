my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('test_4.txt', 'r') as f:
    for i in f:
        i = i.split(' ', 1)
        new_file.append(my_dict[i[0]] + '  ' + i[1])
    print(new_file)

with open('test_4_translated.txt', 'w') as f_2:
    f_2.writelines(new_file)
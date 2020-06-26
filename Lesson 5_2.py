my_list = ['One\n', 'Two\n', 'Three\n']
with open("test_2.txt", 'w+') as f:
    f.writelines(my_list)
with open("test_2.txt") as f:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"There are {letters} letters in line")
    print(f"There are {lines} lines")
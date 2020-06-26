my_list = []
while True:
    line = input("Enter new text line: ")
    if line == '':
        print(my_list)
        exit()
    else:
        newline = line + '\n'
        my_list.append(newline)

    with open("test_1.txt", "w") as f:
        f.writelines(my_list)
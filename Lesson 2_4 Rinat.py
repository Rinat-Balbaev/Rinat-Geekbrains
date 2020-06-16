user_str = input("Введите строку из нескольких слов: ")
my_word = []
num = 1
for el in range(user_str.count(' ') + 1):
    my_word = user_str.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word [el]}")
        num += 1
    else:
        print(f" {num} {my_word [el] [0:10]}")
        num += 1
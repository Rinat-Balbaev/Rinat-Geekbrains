user_el_number1 = int(input("Введите количество элементов: "))
my_list1 = []
i = 0
el = 0
while i < user_el_number1:
    my_list1.append(input("Введите значение следующего элемента "))
    i += 1

for elem in range(int(len(my_list1)/2)):
        my_list1[el], my_list1[el + 1] = my_list1 [el + 1], my_list1[el]
        el += 2
print(my_list1)
# Задача "Нули ничто, отрицание недопустимо!"
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while my_list[i] >= 0:
    if my_list[i] == 0:
        i = i + 1
        if i == len(my_list):
            break
        continue
    else:
        print(my_list[i])
        i = i + 1
    if i == len(my_list):
        break
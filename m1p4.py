my_string = input("Введите любую фразу: ")
print("Введенная фраза содержит: ",len(my_string),"символов")
print("")
print("Проверяем работу методов строк:")
print("")
print(my_string.upper(), "- перевод в верхний регистр;")
print(my_string.lower(), "- перевод в нижний регистр;")
print(my_string.replace(' ',''), "- удаление пробелов;")
print(my_string[0], "- вывод первого символа строки;")
print(my_string[-1], "- вывод последнего символа строки;")
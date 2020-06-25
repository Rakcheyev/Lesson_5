'''
Задание 2
Пользователь вводит с клавиатуры некоторый текст, 
после чего пользователь вводит список зарезервированных 
слов. Необходимо найти в тексте все зарезервированные 
слова и изменить их регистр на верхний. Вывести на 
экран измененный текст. 
'''
input_string = input("Enter text: ")
input_list = input("Enter words, that needs to ne uppercase (separated by space): ").lower()

words_list = input_list.split()

for x in words_list:
    input_string=input_string.replace(x, x.upper())
print(input_string)

    
'''Задание 1
Пользователь вводит с клавиатуры строку. Проверьте 
является ли введенная строка палиндромом. Палин-
дром — слово или текст, которое читается одинаково 
слева направо и справа налево. Например, кок; А роза 
упала на лапу Азора; доход; А буду я у дуба.
'''
##Ввод слова с заменой пробелов и перевод в нижний регистр
input_string = input("Enter text to check: ").replace(' ', '').lower()

output_string = input_string[::-1]

if output_string == input_string:
    print("This text is palindrome")
else:
    print("It's not a palindrome")

'''

Задание 1
Напишите функцию, которая отображает на экран 
форматированный текст, указанный ниже:
“Don't compare yourself with anyone in this world…
if you do so, you are insulting yourself.”
                                        Bill Gates


'''
str1 = "“Don't compare yourself with anyone in this world…"
str2 = "if you do so, you are insulting yourself.”"
str3 = "Bill Gates"
    
def __formatting__():

    print(         '{: <50}'.format(str1) + \
            '\n' + '{: <50}'.format(str2) + \
            '\n' + '{: >50}'.format(str3))

__formatting__()
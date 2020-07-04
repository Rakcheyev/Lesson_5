'''   

Задание 3
Напишите функцию, которая отображает пустой или 
заполненный квадрат из некоторого символа. Функция 
принимает в качестве параметров: длину стороны ква-
драта, символ и переменную логического типа: 
■ если она равна True, квадрат заполненный;
■ если False, квадрат пустой.
'''
side = int(input("Enter length of any side of a square: "))

def __square__(self, side, c=True):
    for x in range(side):  
        for i in range(side):      
            if c == True:
                print(self, end = ' ')
            else:
                print('', end = ' ')
        print()

__square__('*',side, c=True) ## О передачи значения речи не шло - менять True/False здесь (можно 1/0) и символ тоже если хочется

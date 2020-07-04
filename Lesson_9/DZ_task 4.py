'''
    
Задание 4
Напишите функцию, которая возвращает минимальное 
из пяти чисел. Числа передаются в качестве параметров.
'''

def min_num(*args):
    lst = list(args)
    for i in range(len(lst) - 1):
        first = i
        for j in range( i + 1, len(lst)):
            if(lst[j] < lst[first]):
                first = j
        if(first != i):
            lst[i], lst[first] = lst[first], lst[i]
    print(lst[0])
         
min_num(5,-7,3,22,5)
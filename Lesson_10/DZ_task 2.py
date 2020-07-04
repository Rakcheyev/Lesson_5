'''

Задание 2
Напишите функцию для нахождения минимума в 
списке целых. Список передаётся в качестве параметра. 
Полученный результат возвращается из функции.
'''
def min_num(numbers):
    lst =numbers
    
    for i in range(len(lst) - 1):
        first = i
        for j in range( i + 1, len(lst)):
            if(lst[j] < lst[first]):
                first = j
        if(first != i):
            lst[i], lst[first] = lst[first], lst[i]
    print(lst[0])
         
min_num([5,4,3,22,-5])
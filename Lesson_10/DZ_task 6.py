'''

Задание 6
Напишите функцию, высчитывающую степень каждого 
элемента списка целых. Значение для степени передаётся 
в качестве параметра, список тоже передаётся в качестве 
параметра. Функция возвращает новый список, содержа-
щий полученные результаты.
'''

def square(nums, square_arg):
    out = []
    out.append([i ** square_arg for i in nums])
    print(out)

square([1,4,8,2],2)
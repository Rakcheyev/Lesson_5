'''

Задание 5
Напишите функцию, которая получает два списка в 
качестве параметра и возвращает список, содержащий 
элементы обоих списков.

'''

def intersect(lst1,lst2):
    common_lst = [i for i in lst1 if i in lst2]

    print(common_lst)

intersect([1,4,25,2,4,99,22],[4,5,2,99,4,7])
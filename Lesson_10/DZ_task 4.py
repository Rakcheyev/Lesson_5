'''

Задание 4
Напишите функцию, удаляющую из списка целых 
некоторое заданное число. Из функции нужно вернуть 
количество удаленных элементов.
'''

def del_num(nums, num_to_del):
    lst = []
    for i in nums:
        if i != num_to_del:
            lst.append(i)
        else:
            continue
    count_del = len(nums) - len(lst)
    print(count_del)

del_num([1,21,5,36,21,4,21,21], 21)
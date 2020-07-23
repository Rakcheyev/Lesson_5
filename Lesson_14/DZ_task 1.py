def equal_nums(t1, t2, t3):
    ''' Задание 1
    Есть три кортежа целых чисел необходимо найти
    элементы, которые есть во всех кортежах.
    '''

    lst = []
    for i in t1:
        if i in t2 and i in t3:
            lst.append(i)
    print(lst)

t1 = (1,5,3,4,2,12)
t2 = (2,3,15,12,0)
t3 = (6,3,8,9,12)

equal_nums(t1, t2, t3)


# def equal_nums(t1, t2, t3):
#     ''' то же но сетами

#     '''

#     result = tuple(set(t1) & set(t2) & set(t3))
#     print(result)

# t1 = (1,5,3,4,2,12)
# t2 = (2,3,15,12,0)
# t3 = (6,3,8,9,12)

# equal_nums(t1, t2, t3)



def equal_in_place(t1, t2, t3):
    ''' Задание 3
    Есть три кортежа целых чисел необходимо найти эле-
    менты, которые есть в каждом из кортежей и находятся
    в каждом из кортежей на той же позиции.
    '''

    result = []
    min_len = min(len(t1),len(t2),len(t3))
    
    for i in range(min_len):
        if t1[i] == t2[i] == t3[i]:
            result.append(t1[i])
    print(result)

t1 = (1,3,4,2,12,8,10)
t2 = (2,3,15,12,0,8,22)
t3 = (6,3,8,9,12,8,22)

equal_in_place(t1, t2, t3)

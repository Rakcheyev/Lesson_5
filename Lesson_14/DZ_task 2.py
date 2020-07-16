def unique(t1,t2,t3): 
    ''' Задание 2
    Есть три кортежа целых чисел необходимо найти
    элементы, которые уникальны для каждого списка.
    '''
    
    t_total = t1 + t2 + t3
    result = []   
    for i in range(len(t_total)):
        if t_total.count(t_total[i]) == 1:
            result.append(t_total[i])
        # print(f"{t_total.count(t_total[i])} of {t_total[i]}")
    print(result)

t1 = (1,5,3,4,2,12)
t2 = (2,3,15,12,0)
t3 = (6,3,8,9,12)

unique(t1,t2,t3)


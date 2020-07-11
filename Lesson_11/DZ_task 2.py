def summarize(a):     
    """ Продемонструвати:2. Що таке map """

    return a + a

numbers = (5,1,2,7) # передаем последовательность чисел для использования map 
result1 = list(map(summarize, numbers)) # возвращает список из примененной функции к каждому элементу списка

print(result1)

def filt(x):
    """ Продемонструвати:2. Що таке filter """

    if x > 5:
        return 1 # True
    else:
        return 0 # False

result2 = list(filter(filt, result1)) # Убрал значение больше 5 из результата предыдущей функции

def pow_func(x):     
    """ Продемонструвати:2. Що таке lambda x: x ** 2 """

    return x ** 2

print(f"Result of regular user function is: {pow_func(9)}")

pow = lambda x: x ** 2

print(f"Result of lambda function is: {pow(9)}")

    """ Основные отличия - лямбда не создает имени, а возвращает объект.
        Для повторного вызова/обращения к лямбда функции обязательно использование
        переменной в качестве привязки.
        Их не любят ООПшники ((.

    """    
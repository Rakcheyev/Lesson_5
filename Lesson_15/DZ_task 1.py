from random import randint

def diff_nums(*args):
    ''' 1. Різні елементи для A, B '''

    result = A - B

    print(result)


def common_nums(*args):
    ''' 2. Однакові елементи для A, C '''

    result = A & C

    print(result)


def union_nums(*args):
    ''' 3. Об'єднання всіх трьох множин. '''

    result = A | B | C
    # res2 = res1 - C

    # final_res = list(res2)
    print(result)


# Створити множини: A, B, C з довільними елементами.
A = set([randint(15, 45) for i in range(10)])
B = set([randint(15, 45) for i in range(10)])
C = set([randint(15, 45) for i in range(10)])

diff_nums(A,B,C)
common_nums(A,B,C)
union_nums(A,B,C)
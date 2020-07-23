# A = {'a', 4, 'text'}
# print(A)

# A = {1, 2, 3, 4, 5, 6}
# print(A)

# A = set()
# print(type(A))

# A = {1, 2, 7, 4, 5, 6}
# B = {7, 6, 3, 1, 12, 2}

# print(3 in A)
# print(4 in B)

# print(A - B)
# print(B - A)
# print(A | B)
# print(A & B)
# print(A ^ B)

# from random import randint

# lst_1 = [randint(1, 1000) for i in range(10000)]
# lst_2 = [randint(1, 1000) for i in range(10000)]

# A = set(lst_1)
# print('~' * 20)
# B = set(lst_2)

# x = int(input())
# if x in A | B:
#     print("Found")
# else:
#     print("Not found")

# from random import choice

# def get_rand_string(length: int) -> str:
#     result = ""
#     # suff = "@mail.com"

#     for i in range(length):
#             result += choice(alphabet)
#     return result 

# alphabet = ['a','b','c','d','e','f', 'g']

# lst1 = [get_rand_string(length=len(alphabet)) for i in range(100)]
# lst2 = [get_rand_string(length=len(alphabet)) for i in range(100)]

# A = set(lst1)
# B = set(lst2)

# text = input("Enter some text: ")

# if text in (A | B):
#     print("Found")
# else:
#     print("Not found")

A = {1,2,3,4,5,7,9,12}
B = {6,8}
V = {1,2,3}

C = A.union(B)
D = A.intersection(B)
F = A.symmetric_difference(B)

# flag = A > V
A.remove(12) 
# A.superset(V)  
# V.issubset(A)  
# A.isdisjoint(B)  
# A.difference(V)  
# A.update(B) A |= B 
# K = B.copy() 
# A.intersection_update(V) A &= V 
# A.difference_update(V) A-= V
# A.add(22) 

print(A)
    










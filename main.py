'''
big_num = -9999999999

number = int(input("Enter a number or -1 to close program: "))
while number != -1:
    if number > big_num:
        big_num = number
    number = int(input("Enter a number or -1 to close program: "))
print("The biggest number: ", big_num)

i = 0
while i < 100:
    print("i =", i)
    i += 1
print("Loop end... i =", i)

for i in range(0, 100, 1):
    print(i)
    pass

for i in range(1,6):
    if i == 3:
        break
    print("Я в цикле.", i)
print("Я вне цикла.")

for i in range(1,6):
    if i == 3:
        continue
    print("Я в цикле.", i)
print("Я вне цикла.")

big_num = -999999

i = 0
while True:
    number = int(input("Введите число: "))
    
    if number == -1:
        break
    elif number > big_num:
        big_num = number
else:
    pass

ll = [1, 2, 3, 6, 3, 2]
ll_2 = []

for i in ll:
    if i == 2:
        continue
    ll_2.append(i)

print(ll_2)

for i in "Hello world":
    print(i)


word = 'apple'
word_2 = ''
word_3 = 'I\'m Dima'

print(len(word))
print(len(word_2))
print(len(word_3))

example = 'silly walks'

for i in range(len(example)):
    print(example[i], end=' ')
    print(example[::-1])

example = 'silly walks'

print(example.count('s'))

шифр цезаря
буквы маленькие

lst1 = [1,2,3]
lst2 = ['a','b','c']

whole = ['a',1,8,'b',3,'c']
strs = list(filter(lambda x: type(x) == str, whole))
ints = list(filter(lambda x: type(x) == int, whole))

whole = sorted(strs) + sorted(ints)
print(whole)

whole.append('Hello')
print(whole)

whole.remove(2)
print(whole)

del whole[-1]



whole.pop(1)
print(whole)

whole.reverse()
print(whole)

whole.insert(3, 'blah..blah')
print(whole)

lst3 = [55,89]
whole.extend(lst3)
print(whole)

index = whole.index('c')
print(index)

whole.clear()
print(whole)


lst = [1,2,3,4,5]
price = 0

for i in lst:
    price += i
    print(price)

a = 10
b = 20

a,b = b,a

print(a, b)


lst = [10,2,8,4,1]
x = 1
while x < len(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
    x +=1
print(sorted(lst))
        

##срезы, слайсы, многомерные массивы.

whole = ['a',1 ,8,'b', 3,'c']
strs = list(filter(lambda x: type(x) == str, whole))
ints = list(filter(lambda x: type(x) == int, whole))

whole = sorted(strs) + sorted(ints)
print(whole)



list_1 = [20,30,2,5,6,22,14]

to_find = 22
found = False
for i in range(len(list_1)):
    found = list_1[i] == to_find
    if found:
        print(f"Your index is {i}")
        break
else:
    print("Not found")



row = [i for i in range(8) if i % 3 == 0]
print(row)

board = []
for i in range(8):
    row = [i for i in range(8)]
    board.append(row)

print(board)

board = []
row = []
board = [["" for i in range(8)] for j in range(8)]

board[0][1] = "Knight"
    
print(board)

print("Hello world")

print(f"Hello {6}")
        



      

def foo():

    for i in range(5):
        print(i)

if __name__ == "__main__":
    i = 10

    foo()

    print(i)


import sys

print(sys.__dict__.keys())

class Enemy:
    def __init__(self):
        self.hp = 100
    def kick(self):
        self.hp -= 10
        def some_damage(self):
            hp = 1000
            print(hp)
            self.hp -= 5
        some_damage(self)

if __name__ == "__main__":
    e = Enemy()
    print(e.hp)
    e.kick()
    print(e.hp)


print(dir(__builtins__))

'''
'''

Задание 3
Напишите функцию, определяющую количество про-
стых чисел в списке целых. Список передаётся в качестве 
параметра. Полученный результат возвращается из функции.
'''


'''

def simple(self):
    lst = []
    for i in range(2, self+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
          
    print(self)

simple([1,3,5,10,9])
'''

# def abs(a: int):
#     return a ** 2

# a =  -20
# a = abs(a)

# print(a)

# def foo():
#     print("Hello")

# bar = foo

# print(foo())
# print(bar())


# two = lambda : 2

# print(two())

# def sqrt(x: int):
#     return x ** 2

# a = sqrt(4)

# print(a)

# lst = [1,2,3,4,5,6]
# lst_2 = map(lambda x: x ** 2, lst)

# def helper(x):
#     return x ** 2

# print(lst)
# lst2 = map(helper, lst)
# print(list(lst2))


# a = [1, 2, 3, 4, 5, 6, True, False, "Hello", "Python"]
# # b = filter(lambda x : x % 2 == 0, a) 

# # # print(list(b))

# # def foo(x):

# #     if type(x) == int:
# #         if x < 3 or x == 6:
# #             return True
# #     if type(x) == bool:
# #         if not x:
# #             return True
# #     if type(x) == str:
# #         if "n" in x:
# #             return True
# #     else:
# #         return False
             

# # b = filter(foo, a)

# # print(list(b))

# b = filter((lambda x : type(x) == int and (x < 3 or x == 6) or x == False or "n" in str(x)), a)

# print(list(b))

# def outer(par):
#     loc = par
    
#     def inner():
#         return loc
#     return inner()
# var = 1
# a = outer(var)

# # print(par)
# print(a)
    
'''
'''
# Bubble sort

# def bubble(lst):
#     n = len(lst)

#     for i in range(n):
#         sorted = True

#         for x in range(n - i - 1):
#             if lst[x] > lst[x + 1]:
#                 lst[x], lst[x + 1] = lst[x + 1], lst[x]
#                 sorted = False

#         if sorted:
#             break

#     return lst

# print(bubble([2,5,3,1,6,-4,10,5]))

# def bubble(nums):
#     sorted = True

#     while sorted:
#         sorted = False
        
#         for i in range(len(nums) - 1):
#             if nums[i] > nums[i + 1]:
#                 nums[i], nums[i + 1] = nums[i + 1], nums[i]
#                 print(f' {nums[i + 1]} > {nums[i]} swap {nums[i]} >< {nums[i + 1]}')
#                 sorted = True
#             else:
#                 print(f' {nums[i]} > {nums[i + 1]} skip -->')    
#     return nums

# print(bubble([-1,2,1,-4,9,8]))


# l = []

# while True:
#     t = input("Enter some text: ")
#     if not t:
#         break
    
#     l.append(t)

# res = []
# for element in l:
#     for letter in set(element):
#         if element.count(letter) == 2:
#             res.append(element)

#             break
            
        
# print(res)

# Selection sort

# def selection_sort(nums: list):
#     for i in range(len(nums)):
#         lowerest_index = i
#         print(f"iteration {i}")
#         for j in range(i + 1, len(nums)):
#             print(f"Compare {nums[j]} < {nums[lowerest_index]}")
#             if nums[j] < nums[lowerest_index]:
#                 lowerest_index = j
#         nums[i], nums[lowerest_index] = nums[lowerest_index], nums[i]

#         print(nums)
#         print("*"*10)

# l = [12, 8, 3, 20, 11]
# print(l)
# selection_sort(l)
# print(l)



# def insertion_sort(nums, left=0, right=None):
#     if right is None:
#         right = len(l) - 1

#     for i in range(left + 1, right + 1):
#         key_item = nums[i]

#         j = i - 1

#         while j >= left and nums[j] > key_item:

#             nums[j + 1] = nums[j]
#             j -= 1
#             print(nums)

#         nums[j + 1] = key_item
#         print(nums)
#     return nums

# l = [9, 1, 15, 28, 6]
# print(insertion_sort(l))

# Insertion sort


# def insertion_sort(lst):

#     for i in range(1, len(lst)):

#         key_item = lst[i]

#         x = i - 1

#         while x >= 0 and lst[x] > key_item:
#             lst[x + 1] = lst[x]
#             x -= 1

#         lst[x + 1] = key_item

#     return lst

# # Merge sort
#     def merge(left, right):

#     if len(left) == 0:
#         return right

#     if len(right) == 0:
#         return left

#     result = []
#     index_left = index_right = 0

#     while len(result) < len(left) + len(right):
#         if left[index_left] <= right[index_right]:
#             result.append(left[index_left])
#             index_left += 1
#         else:
#             result.append(right[index_right])
#             index_right += 1

#         if index_right == len(right):
#             result += left[index_left:]
#             break

#         if index_left == len(left):
#             result += right[index_right:]
#             break

#     return result

# # Quicksort

# from random import randint

# def quicksort(lst):

#     if len(lst) < 2:
#         return lst

#     lower, same, higher = [], [], []

#     pivot = lst[randint(0, len(lst) - 1)]

#     for item in lst:
#         if item < pivot:
#             lower.append(item)
#         elif item == pivot:
#             same.append(item)
#         elif item > pivot:
#             higher.append(item)

#     return quicksort(lower) + same + quicksort(higher)

# print(quicksort([1,2,5,1,9,-5,0,56,19,5,88]))

# t3 = (1, 2, [1, 2, 3], False)

# t3[2][1]=3

# print(t3)

# from random import randint

# t = ()
# lst = []

# for i in range(5):
#     lst.append(randint(0, 10))
# t = t(lst)

# print(t)

# i = int(input("Enter sequence length "))


# a = 0
# b = 1
# count = 0

# if i <= 0:
#    print("Please enter a positive integer")
# elif i == 1:
#    print(f"Fibonacci sequence upto {i} :")
#    print(a)
# else:
#    print("Fibonacci sequence:")
#    while count < i:
#        print(a)
#        seq = a + b

#        a = b
#        b = seq
#        count += 1


# def recur_fib(n):

#     if n <= 1:
#         return n
#     else:
#         return(recur_fib(n-1) + recur_fib(n-2))

# seq = 10

# if seq <= 0:
#     print("Plese enter a positive integer")
# else:
#     print("Fibonacci sequence:")
#     for i in range(seq):
#         print(recur_fib(i))


# num = int(input("Enter a number: "))
 
# fact = 1
# i = 1
 
# while i <= num:
# 	fact = fact * i
# 	i = i + 1
 
# print("facttorial of ", num, " is ", fact)


# def fact(n):
#     if n == 1:
#         return n
#     else:
#         return n * fact(n-1)

# print(fact(5))
'''
t1 = (1, 4, 8, 3, 0, 11)
t2 = (1, 6, 7, 3, 3)
t3 = (1, 4, 2, 3)



# The same tuples for all tasks
t1 = (1, 4, 8, 3,5,8)
t2 = (1, 6, 7, 3,4,8)
t3 = (1, 4, 2, 3,5,8)
print(f"Tuple 1: {t1}\nTuple 2: {t2}\nTuple 3: {t3}")
def same_index(t1, t2, t3):
    """Returns the same index of numbers with the same number"""
    for index, num in enumerate(t1):
        if t1[index] == t2[index] == t3[index]:
            print(f"The index of number ({num}) is {index}")
print("\nTask 3:")
same_index(t1, t2, t3)

'''

# The same tuples for all tasks
t1 = (1, 4, 8, 3)
t2 = (1, 6, 7, 3)
t3 = (1, 4, 2, 3)
print(f"Tuple 1: {t1}\nTuple 2: {t2}\nTuple 3: {t3}")
def same_index(t1, t2, t3):
    """Returns the same index of numbers with the same number"""
    for n, index in enumerate(t1, 0):

        print(n, index)

print("\nTask 3:")
same_index(t1, t2, t3)
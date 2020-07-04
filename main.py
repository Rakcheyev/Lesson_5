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

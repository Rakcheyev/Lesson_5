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

'''


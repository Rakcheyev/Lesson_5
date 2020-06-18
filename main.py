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

'''

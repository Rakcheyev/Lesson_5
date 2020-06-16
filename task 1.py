'''Завдання 1
Користувач вводить 3 числа. Далі в залежності від вибору користувача 
потрібно знайти суму або добуток цих чисел. 
(Тобто програма запитує в користувача, що потрібно зробити)'''
a = int(input("Input first number :"))
b = int(input("Input second number :"))
c = int(input("Input third number :"))

action = input("Choose action (+ or *): ")

if action == "+":
    print("The answer is: " + str(a+b+c))
else:
    print("The answer is: " + str(a*b*c))

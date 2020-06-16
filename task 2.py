<<<<<<< HEAD
'''Завдання 2
Користувач вводить 3 числа. Далі в залежності від вибору користувача 
потрібно знайти найбільше з 3-х, найменше, або середнє арифметичне. 
(Подібно до 1-го)'''

a = int(input("Input first number :"))
b = int(input("Input second number :"))
c = int(input("Input third number :"))

comparation = input("Select comparation (max or min or avg): ")

if comparation == "max":
    print("Maximal number is : " + str(max(a, b, c)))
elif comparation == "min":
    print("Minimal number is : " + str(min(a, b, c)))
else:
    print("Average number is : " + str((a + b + c) / 3))
=======
'''Завдання 2
Користувач вводить 3 числа. Далі в залежності від вибору користувача 
потрібно знайти найбільше з 3-х, найменше, або середнє арифметичне. 
(Подібно до 1-го)'''

a = int(input("Input first number :"))
b = int(input("Input second number :"))
c = int(input("Input third number :"))

comparation = input("Select comparation (max or min or avg): ")

if comparation == "max":
    print("Maximal number is : " + str(max(a, b, c)))
elif comparation == "min":
    print("Minimal number is : " + str(min(a, b, c)))
else:
    print("Average number is : " + str((a + b + c) / 3))
>>>>>>> e9e718f11c61d14cee634a760c3b1766b07cc039

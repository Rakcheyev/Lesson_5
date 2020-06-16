'''Завдання 3
Користувач вводить з клавіатури кількість метрів. 
В залежності від вибору - програма конвертує їх в 
сантиметри, міліметри, або кілометри.'''

a = int(input("Input number of meters :"))

convertion = input("Select convertion type \nc - centimeters\n\
m - millimeters\nk – kilometers :")

if convertion == "c":
    print("It's equal - " + str(a * 100) + " centimeters")
elif convertion == "m":
    print("It's equal - " + str(a * 1000) + " millimeters")
else:
    print("It's equal - " + str(a / 1000) + " kilometers")

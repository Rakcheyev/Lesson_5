'''

Задание 2
Напишите функцию, которая принимает два числа 
в качестве параметра и отображает все четные числа 
между ними.

'''

num1 = int(input("Enter starting number: "))
num2 = int(input("Enter starting number: "))

def __even__():
    for i in range(num1 + 1, num2):
        if (i % 2) == 0:
            print(f"{i} is even")
        else:
            continue
            
__even__()  
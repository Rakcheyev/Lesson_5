def pow(func):
    ''' 1. Написати функцію-декоратор, яка підносить до квадрату значення, 
        що повертає функція, до якої декоратор застосовується. 
    '''
    
    def wrapper(num):
        if type(num) != int:
            print("Please, enter a number!")
        else:
            return num ** 2
        return func(num)
    return wrapper
    
@pow
def inp(num):
    return num

print(inp(3))
    
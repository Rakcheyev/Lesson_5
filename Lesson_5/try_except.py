try :
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ValueError:
    print("You need to enter a number!!!")
except:
    print("Something was wrong!!!")
    
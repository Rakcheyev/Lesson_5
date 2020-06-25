'''
Задание 1
Два списка целых заполняются случайными числами. 
Необходимо:
'''
import random 

random_lst = []
random_lst2 = []

random_lst3 = []

for i in range(0,10):
    n = random.randint(1,20)
    random_lst.append(n)
print(f"first list = {random_lst}")

for i in range(0,10):
    n = random.randint(15,25)
    random_lst2.append(n)
print(f"second list = {random_lst2}")

##■ Сформировать третий список, содержащий элементы обоих списков;
random_lst3 = random_lst + random_lst2
print(f"all in one = {random_lst3}")
random_lst3.clear()

##■ Сформировать третий список, содержащий элементы обоих списков без повторений;
random_lst3 = list(random_lst)
random_lst3.extend(i for i in random_lst2 if i not in random_lst3)
    
print(f"without dups = {random_lst3}")
random_lst3.clear()
##■ Сформировать третий список, содержащий элементы общие для двух списков;        
random_lst3 = list(set(random_lst).intersection(random_lst2))
    
print(f"dups only = {random_lst3}")
random_lst3.clear()

##■ Сформировать третий список, содержащий только уникальные элементы каждого из списков;
temp_lst = (random_lst + random_lst2)

for x in temp_lst:
    if x not in random_lst or x not in random_lst2:
        random_lst3.append(x)

print(f"uniques only = {random_lst3}")
random_lst3.clear()

##■ Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.
random_lst = sorted(random_lst)
random_lst2 = sorted(random_lst2)

tup = (random_lst[0],random_lst[-1],random_lst2[0],random_lst2[-1])
random_lst3 = list(tup)

print(f"min/max only = {random_lst3}")



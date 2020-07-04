'''

Задание 3
Напишите функцию, определяющую количество про-
стых чисел в списке целых. Список передаётся в качестве 
параметра. Полученный результат возвращается из функции.
'''

def count_primes(nums):
    lst = []
    
    for num in nums:
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            # print(num)
            lst.append(num)
    return len(lst)

print(count_primes([1,2,3,4,5,6,8,9,10]))
    

                    
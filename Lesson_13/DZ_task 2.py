from time import time

def print_execution_time(function):
    ''' Было интересно сделать замер по разным подходам
        пример со стеками, если я все правильно вывел в таймере оптимальнее
        пример был с косяками в типах данных и без корректного форматирования.

        Пока самый быстрый. 
        ВНимание - превью на нем крашит VS Code. о_0 Из-за постоянного
        чтения таймера. Возможно не корректно написан.
    '''

    def timed(*args, **kw):
        time_start = time()
        return_value = function(*args, **kw)
        time_end = time()

        execution_time = time_end - time_start

        print("{} ms {}".format(str(execution_time * 1000), function.__name__))
        return return_value

    return timed

@print_execution_time
def quick_sort_less_iter(nums):
    ''' Реалізувати Швидке сортування: '''

    w = [x for x in range(len(nums) -1)] #стек по длине списка
    k = 0 #старт
    w[0] = k # указатель на позицию левой границы половины
    w[1] = len(nums) - 1 # указатель на позицию правой границы половины
    while (k >= 0):
        i = quick_sort_pos(nums, w[k], w[k + 1])
        if i != w[k + 1]:
            RL = i + 1 # левая граница правого подъинтервала
        else:
            RL = w[k + 1]
        RR = w[k + 1] # Правая граница правого подъинтервала
        LL = w[k] # Левая граница левого подъинтервал
        if i != w[k]:
            LR = i - 1 #Правая граница левого подъинтервал
        else:
            LR =w[k]
        k -= 2 # выход за границы для удаления интервала
        if RL != RR:
            k += 2
            w[k] = RL
            w[k + 1] = RR
        if LL != LR:
            k += 2
            w[k] = LL
            w[k + 1] = LR
    return nums

@print_execution_time
def quick_sort_pos(nums, left, right):
    i = left
    j = right - 1
    while (True): # чтобы поставить разделяющий элемент на свое место
        while nums[i] < nums[right]: 
            i += 1
        while nums[j] > nums[right] and j > left: 
            j -= 1
        if i >= j: 
            break
        nums[i],nums[j] = nums[j],nums[i]
    nums[right],nums[i] = nums[i],nums[right]
    return i


print(quick_sort_less_iter([-1,-3,5,5,6,8,12,1,0,3,4,15,3,4,15,1,12,13]))

    ''' раскомментировать следующий для теста! пример не мой - w3 типа стандартный
    мне кажется где то косяк
    '''


# @print_execution_time
# def quick_sort_usual(nums):
#    quick_sort_help(nums, 0, len(nums)-1)

# @print_execution_time
# def quick_sort_help(nums, first, last):
#    if first < last:

#        splitpoint = partition(nums, first, last)

#        quick_sort_help(nums, first, splitpoint - 1)
#        quick_sort_help(nums, splitpoint + 1, last)

# @print_execution_time
# def partition(nums,first,last):
#    pivotvalue = nums[first]

#    left = first + 1
#    right = last

#    done = False
#    while not done:

#        while left <= right and nums[left] <= pivotvalue:
#            left = left + 1

#        while nums[right] >= pivotvalue and right >= left:
#            right = right - 1

#        if right < left:
#            done = True
#        else:
#            temp = nums[left]
#            nums[left] = nums[right]
#            nums[right] = temp

#    temp = nums[first]
#    nums[first] = nums[right]
#    nums[right] = temp


#    return right

# nums = [-1,-3,5,5,6,8,12,1,0,3,4,15,3,4,15,1,12,13]
# quick_sort_usual(nums)
# print(nums)


# Bubble sort

def bubble(nums):
    sorted = True

    while sorted:
        sorted = False
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                print(f' {nums[i + 1]} > {nums[i]} is True then swap = {nums[i]} >< {nums[i + 1]}')
                sorted = True
            else:
                print(f' {nums[i]} > {nums[i + 1]} is False then skip -->')    
    return nums

print(bubble([-1,2,1,-4,9,8]))
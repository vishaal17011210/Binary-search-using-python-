# To create the random number
import random
def Create_the_randm_number_list(count ,lower_number,higher_number):
    random_numbers = []
    for _ in range(count):
        num = random.randint(lower_number,higher_number)
        random_numbers.append(num)
    return random_numbers
# To Cheak the number where in the list 
def binary_search(arr , target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        mid_value = arr[mid]
        if mid_value == target:
            return mid_value
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 
count = 10 
lower_number = 1
higher_number = 100
random_numbers = Create_the_randm_number_list(count,lower_number,higher_number)
print(f'The random number list :  {random_numbers}')
random_numbers.sort()
print(f'The random number list after sort : {random_numbers}')
target = int(input('Enter the target number : '))
result = binary_search(random_numbers,target)
if result != -1:
    print(f'The target number is found : {result}')
else:
    print('The target is not found')
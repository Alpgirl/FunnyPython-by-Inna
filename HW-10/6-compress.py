from random import randint

N = int(input("Введите кол-во чисел в списке: "))
nums = [randint(-5,5) for i in range(N)]
print("Старый список:", nums)

nums_new = [nums.append(nums.pop(nums.index(value))) for value in nums if value == 0]
if nums_new:
    nums = nums[:-len(nums_new)+1:1]

print("Новый список:", nums)
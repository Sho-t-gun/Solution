def sum_of_neighbors(numbers):
    nums = list(map(int, numbers.split()))
    if len(nums) == 1:
        return str(nums[0])
    return ' '.join(str(nums[i-1] + nums[(i+1) % len(nums)]) for i in range(len(nums)))

input_numbers = "99 8 5 17 80"
result = sum_of_neighbors(input_numbers)
print(result)
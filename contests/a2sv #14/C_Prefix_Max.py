t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    # Calculate value of original array
    def calculate_value(arr):
        total = 0
        current_max = 0
        for x in arr:
            if x > current_max:
                current_max = x
            total += current_max
        return total

    original_value = calculate_value(nums)
    
    # Try swapping the first element with the maximum element
    max_num = max(nums)
    max_index = nums.index(max_num)
    
    best_value = original_value
    
    if max_index != 0:
        # Perform swap
        nums, nums[max_index] = nums[max_index], nums
        swapped_value = calculate_value(nums)
        best_value = max(original_value, swapped_value)
        
    print(best_value)

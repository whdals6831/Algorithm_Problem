def maxSubArray(nums):
    max_values = [0] * (len(nums)+1)
    max_result = 0

    idx = 0

    for num in nums:
        idx += 1
        max_values[idx] = num

        if max_values[idx] < max_values[idx-1] + num:
            max_values[idx] = max_values[idx-1] + num

        if idx == 1 or max_result < max_values[idx]:
            max_result = max_values[idx]

    return max_result
    

print(maxSubArray([-1, 4, -2, 6, -10]))
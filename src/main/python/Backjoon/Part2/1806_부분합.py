import math

n, k = map(int, input().split())
nums = list(map(int, input().split()))
min_len = float('inf')
start = 0
end = 0
result = nums[0]

while start < n:
    if result >= k:
        min_len = min(min_len, end-start+1)
        result -= nums[start]
        start += 1
    elif result < k:
        if end+1 < n:
            end += 1
            result += nums[end]
        else:
            break

if math.isinf(min_len):
    print(0)
else:
    print(min_len)
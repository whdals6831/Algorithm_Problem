def quick_sort(nums) :
    if len(nums) <= 1 :
        return nums

    # 최악의 경우를 피하는 pivot 정하는 법
    # 왼쪽, 오른쪽, 가운데값 중에서 중앙값을 pivot
    pivots = [
        nums[0],
        nums[(len(nums)-1)//2],
        nums[(len(nums)-1)]
    ]

    pivot = sum(pivots) - max(pivots) - min(pivots)

    # 피봇을 정하는 가장 간단한 방법
    # pivot = nums[0]

    less_list = []
    more_list = []
    equal_list = []

    for n in nums :
        if n < pivot : 
            less_list.append(n)
        elif n > pivot:
            more_list.append(n)
        else :
            equal_list.append(n)

    return quick_sort(less_list) + equal_list + quick_sort(more_list)



nums = [5,3,8,4,9,1,6,2,7]
print(quick_sort(nums))
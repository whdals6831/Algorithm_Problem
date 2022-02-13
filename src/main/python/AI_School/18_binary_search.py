# 5
# 4 1 5 2 3 
# 5
# 1 3 7 9 5

def b_search(find_num, num_list, start_idx, end_idx) :
    if start_idx > end_idx :
        return -1

    mid_idx = (end_idx + start_idx) // 2

    if find_num < num_list[mid_idx] :
        return b_search(find_num, num_list, start_idx, mid_idx-1)
    elif find_num > num_list[mid_idx] :
        return b_search(find_num, num_list, mid_idx+1, end_idx)

    return mid_idx


n = int(input())
a_list = sorted(list(map(int, input().split())))
m = int(input())
x_list = list(map(int, input().split()))

# a_list.sort()

for find_num in x_list :
    if b_search(find_num, a_list, 0, len(a_list)-1) >= 0 :
        print('1')
    else :
        print('0')
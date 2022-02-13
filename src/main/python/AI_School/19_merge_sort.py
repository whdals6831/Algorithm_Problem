import sys
input = sys.stdin.readline

def combine(num_list, start_idx, mid_idx, end_idx) :
    l_idx = start_idx
    r_idx = mid_idx+1

    sorted_list = []

    while l_idx <= mid_idx and r_idx <= end_idx :
        if num_list[l_idx] < num_list[r_idx] :
            sorted_list.append(num_list[l_idx])
            l_idx += 1
        else :
            sorted_list.append(num_list[r_idx])
            r_idx += 1
    
    # 뒤에 남은 배열 붙혀넣기,
    # 빈 리스트는 들어가는 값이 없어 예외처리가 필요없음
    sorted_list += num_list[r_idx:end_idx+1]
    sorted_list += num_list[l_idx:mid_idx+1]

    # 정렬값 업데이트 
    num_list[start_idx:end_idx+1] = sorted_list


def merge_sort(num_list, start_idx, end_idx) :
    if start_idx >= end_idx :
        return

    mid_idx = (start_idx + end_idx) // 2

    merge_sort(num_list, start_idx, mid_idx)
    merge_sort(num_list, mid_idx+1, end_idx)

    combine(num_list, start_idx, mid_idx, end_idx)
    return num_list




n = int(input())
num_list = []

for _ in range(n) :
    num_list.append(int(input()))


sorted_num_list = merge_sort(num_list, 0, len(num_list)-1)

for i in sorted_num_list:
    print(i)
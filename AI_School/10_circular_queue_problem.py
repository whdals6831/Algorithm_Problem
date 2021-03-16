import sys
from collections import deque

input = sys.stdin.readline


def find_index(dec, num) :
    index = 0

    for i in dec :
        if i == num :
            return index
        
        index += 1
    return print("찾으시는 번호가 없습니다.")


def main() :
    N, M = map(int, input().split())
    result = 0

    dec = deque(range(1, N+1))
    pop_list = list(map(int, input().split()))

    for pop_num in pop_list :  
        left_move_count = find_index(dec, pop_num)
        right_move_count = len(dec) - left_move_count

        if left_move_count <= right_move_count :
            dec.rotate(-left_move_count)
            result += left_move_count
        else :
            dec.rotate(right_move_count)
            result += right_move_count
            
        dec.popleft()

    print(result)

        
main()
import sys

input = sys.stdin.readline

from collections import deque

n = int(input())

# O(N)

# array_list = deque(range(1, n+1))

# while len(array_list) != 1 :
#     a = array_list.popleft()
#     # card_list.rotate(-1) 이 한줄로 밑에줄을 대체할 수 있다.
#     b = array_list.popleft()
#     array_list.append(b)

# print(array_list[0])


# 다른 방법 O(logN)

pow_val = 1

while pow_val < n :
    # 자기보다 크면서 제일 가까운 제곱수 구하기
    pow_val *= 2 

print(n*2 - pow_val)


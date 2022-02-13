# priorities	location	return
# [2, 1, 3, 2]	2	1
# [1, 1, 9, 1, 1, 1]	0	5

from collections import deque

def solution(priorities, location): # deque를 활용한 풀이
    answer = 0

    priority_and_index = deque([(v, i) for i, v in enumerate(priorities)])

    while True:
        item = priority_and_index.popleft()
        
        # popleft한 후 priority_and_index를 참조하면 아무것도 없으면서 runtime error가
        # 발생하게 되므로 존재여부 확인을 위해 if 조건에 priority_and_index를 추가 
        if priority_and_index and max(priority_and_index)[0] > item[0]:
            priority_and_index.append(item)
        else:
            answer += 1

            if item[1] == location:
                break
    return answer

# def solution(priorities, location): # 처음 시도한 풀이
#     answer = 0
#     sort_priorities = sorted(priorities)
#     target_priority = priorities[location]
#     while True:
#         if location == 0 and target_priority == sort_priorities[-1]:
#             answer += 1
#             break
#         elif sort_priorities[-1] == priorities[0]:
#             sort_priorities.pop()
#             priorities.pop(0)
#             location -= 1
#             answer += 1
#         else:
#             priorities.append(priorities.pop(0))
#             if (location-1) < 0:
#                 location = len(priorities)-1
#             else:
#                 location -= 1 
#     return answer

if __name__ == "__main__":
    print(solution([2, 1, 3, 2], 2))
    print(solution([1, 1, 9, 1, 1, 1], 0))
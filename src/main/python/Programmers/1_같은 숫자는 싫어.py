# arr	answer
# [1,1,3,3,0,1,1]	[1,3,0,1]
# [4,4,4,3,3]	[4,3]

def solution(arr):
    answer = []
    now_value = arr[0]
    answer.append(now_value)
    
    for value in arr[1:]:
        if now_value != value :
            answer.append(value)
            now_value = value
    
    return answer
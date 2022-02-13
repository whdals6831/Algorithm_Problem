# numbers	result
# [2,1,3,4,1]	[2,3,4,5,6,7]
# [5,0,2,7]	[2,5,7,9,12]

def solution(numbers):
    answer = []
    
    for n in range(len(numbers)-1):
        for m in range(n+1, len(numbers)):
            answer.append(numbers[n] + numbers[m])
            
    answer = sorted(list(set(answer)))
        
    return answer
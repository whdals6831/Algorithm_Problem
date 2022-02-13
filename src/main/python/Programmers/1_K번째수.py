# array	commands	return
# [1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]

def solution(array, commands):
    answer = []
    
    for command in commands:
        temp = sorted(array[command[0]-1:command[1]])
        answer.append(temp[command[2]-1])
        
    return answer
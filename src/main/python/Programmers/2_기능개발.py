# progresses	speeds	return
# [93, 30, 55]	[1, 30, 5]	[2, 1]
# [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]

def solution(progresses, speeds):
    answer = []
    complete_days = []
    days = 0

    for i, progress in enumerate(progresses):
        if progress+days*speeds[i] >= 100:
            complete_days.append(days)
            continue
        
        while True:
            if progress+days*speeds[i] < 100:
                days += 1
            else:
                complete_days.append(days)
                break
            
            
    for i, day in enumerate(complete_days):
        if i == 0:
            answer.append(1)
        elif day == complete_days[i-1]:
            answer[-1] = answer[-1] + 1
        else:
            answer.append(1)
    
    return answer
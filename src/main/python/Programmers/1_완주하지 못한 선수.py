# participant	completion	return
# [leo, kiki, eden]	[eden, kiki]	leo
# [marina, josipa, nikola, vinko, filipa]	[josipa, filipa, marina, nikola]	vinko
# [mislav, stanko, mislav, ana]	[stanko, ana, mislav]	

def solution(participant, completion):
    answer = ''
    flag = False
    
    participant.sort()
    completion.sort()
    
    for i in range(len(participant)-1):
        if participant[i] != completion[i]:
            answer = participant[i]
            flag = True
            break
            
    if not flag :
        answer = participant[-1]
            
    return answer
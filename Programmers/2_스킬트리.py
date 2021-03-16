# skill	skill_trees	return
# "CBD"	["BACDE", "CBADF", "AECB", "BDA"]	2

def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        now_idx = 0
        collect_skill_tree = True
        
        for s in skill_tree:
            if s in skill and skill[now_idx] == s:
                now_idx += 1
            elif s in skill and skill[now_idx] != s:
                collect_skill_tree = False
        
        if collect_skill_tree:
            answer += 1
    
    return answer
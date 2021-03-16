# n	lost	reserve	return
# 5	[2, 4]	[1, 3, 5]	5
# 5	[2, 4]	[3]	4
# 3	[3]	[1]	2

import numpy as np

def solution(n, lost, reserve):
    students = np.ones(n+2)
    
    for lost_student in lost:
        if lost_student in reserve:
            reserve.remove(lost_student)
        else:
            students[lost_student] = 0
    
    for reserve_student in reserve:
        if students[reserve_student-1] == 0:
            students[reserve_student-1] = 1
            continue
            
        if students[reserve_student+1] == 0:
            students[reserve_student+1] = 1
            continue
    
    students = np.delete(students, np.where(students == 0))
    
    return len(students)-2
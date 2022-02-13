# answers	return
# [1,2,3,4,5]	[1]
# [1,3,2,4,2]	[1,2,3]

def check(answers, result):
    ans_len = len(answers)
    res_len = len(result)
    ans_cnt = 0
    
    multiply_result_cnt = ans_len // res_len
    slice_result_index = ans_len % res_len
    
    answer_list = result * multiply_result_cnt + result[:slice_result_index]
    
    for idx, answer in enumerate(answers):
        if answer == answer_list[idx]:
            ans_cnt += 1
    
    return ans_cnt

def solution(answers):
    answer = []
    
    max_ans_cnt = 0
    answer_cnt_list = []
    
    first_student = [1,2,3,4,5]
    second_student = [2,1,2,3,2,4,2,5]
    third_student = [3,3,1,1,2,2,4,4,5,5]
    
    answer_cnt_list.append(check(answers, first_student))
    answer_cnt_list.append(check(answers, second_student))
    answer_cnt_list.append(check(answers, third_student))
    
    max_ans_cnt = max(answer_cnt_list)
    
    i = 1
    for student in answer_cnt_list:
        if max_ans_cnt == student:
            answer.append(i)
        i += 1
    
    return answer
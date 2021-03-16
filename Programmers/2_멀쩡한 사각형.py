# W	H	result
# 8	12	80

def solution(w,h):
    answer = 0

    max_num = max(w, h)
    min_num = min(w, h)
    
    remain_num = max_num // min_num

    if max_num == min_num:
        answer = max_num
    elif w == 1 or h == 1:
        answer = max_num
    elif remain_num == 1 and (min_num % 2 == 1):
        answer = 2 * max_num - min_num
    else:
        answer = min_num * (remain_num + 1)

    return w * h - answer

if __name__ == "__main__":
    print(solution(56, 2))
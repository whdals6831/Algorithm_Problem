# def VPS(bracket):
#     temp = []

#     for i in bracket:
#         if i == '(':
#             temp.append(i)
#         elif (len(temp) > 0) and (i == ')'):
#             temp.pop(-1)
#         else:
#             return 'NO'
    
#     if len(temp) > 0:
#         return 'NO'
#     else:
#         return 'YES'


# t = int(input())

# for _ in range(t):
#     bracket = input()
#     print(VPS(bracket))

# 추가 문제! VPS가 되는 모든 모양 출력
def make_vps(now_idx, open_cnt, close_cnt, result_vps_str):
    if open_cnt == 0 and close_cnt == 0:
        print("".join(result_vps_str))
    else :
        if open_cnt > 0:
            result_vps_str[now_idx] = "("
            make_vps(now_idx+1, open_cnt-1, close_cnt+1, result_vps_str)
        if close_cnt > 0:
            result_vps_str[now_idx] = ")"
            make_vps(now_idx+1, open_cnt, close_cnt-1, result_vps_str)

pair_cnt = int(input())
result_vps_str = [""] * (pair_cnt*2)

make_vps(0, pair_cnt, 0, result_vps_str)
import sys
# ord('A') => 65
# chr(65) => 'A'

input = sys.stdin.readline


N, B = input().split()
B = int(B)

# 제일 간단한 방법
print(int(N, B))

# ----------반복문-------------
# result = 0
# char_num_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# for i in range(len(N)) :

#     result += int(char_num_map.find(N[i])) * (B ** (len(N)-1-i))

# print(result)


# ---------재귀-------------
# def get_decimal_num(idx_char, now_idx) :
#     if idx_char.isnumeric() :
#         result = int(idx_char) * (B ** (len(N)-1-now_idx))
#     else :
#         result = (ord(idx_char) - ord('A') + 10) * (B ** (len(N)-1-now_idx))

#     return result

# def decimal_conv(now_idx, N, B) :
#     if now_idx == len(N) :
#         return 0

#     now_val = get_decimal_num(N[now_idx], now_idx)

#     return now_val + decimal_conv(now_idx+1, N, B)

# print(decimal_conv(0, N, B))



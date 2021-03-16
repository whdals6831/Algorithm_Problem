import sys

input = sys.stdin.readline
# quotient, remainder = divmod(N, B)  #  몪, 나머지 쉽게 구하는 법
# ord('A') => 65
# chr(65) => 'A'

N, B = map(int, input().split())

# 재귀로 푸는 방법
def n_conv(quotient, B) :
    if quotient == 0 :
        return ''  # 빈 문자열을 해줘야 NoneType에러가 뜨지 않는다.

    divided_quotient, remainder = divmod(quotient, B)

    if remainder < 10 :
        result = str(remainder) 
    else :
        result = chr(remainder + 55)

    return n_conv(divided_quotient, B) + result

print(n_conv(N, B))


# 반복문으로 푸는 방법
# result = ''

# quotient = N

# while quotient > 0 :
#     quotient, remainder = divmod(quotient, B)

#     if remainder < 10 :
#         result = str(remainder) + result
#     else :
#         result = chr(remainder + 55) + result
    

# print(result)
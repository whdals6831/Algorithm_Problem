n = int(input())
reduce_num_list = [0]
m = 1

def reduce_num_check(n):
    before = float('inf')
    global m
    
    for i, v in enumerate(str(n)):
        # 3000에서 3을 v라 하면 v를 제외한 (나머지 자리수의 길이 -1)이 v보다 크면
        # v 자리수의 값을 1 올려줌  3000 -> 4000
        if len(str(n))-1 != i and len(str(n))-i-1 > int(v):
            m -= m % (10**(len(str(n))-i-1))
            m += 10**(len(str(n))-i-1)
            return 0

        if int(v) < before:
            before = int(v)
        elif len(str(n))-1 >= i+1 and int(v) > int(str(n)[i+1]):
            # 뒷자리 수가 앞자리 수보다 크면 앞자리 수를 1 올려줌
            m -= m % (10**(len(str(n))-i-1))
            m += 10**(len(str(n))-i-1)
            return 0
        else :
            return -1

    return 1


while len(reduce_num_list) <= n and m < 10000000000:
    if reduce_num_check(m) == 1:
        reduce_num_list.append(m)
        m += 1
    elif reduce_num_check(m) == -1:
        m += 1


if len(reduce_num_list) <= n:
    print(-1)
else:
    print(reduce_num_list[n])
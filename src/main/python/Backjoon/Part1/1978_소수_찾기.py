n = int(input())

input_number = list(map(int, input().split()))
prime_number = [i for i in range(1001)]
result = 0

prime_number[1] = 0 # 1은 소수가 아님

# 에라토스테네스의 체
for i in range(2, int(1000 ** 0.5)):
    if prime_number[i] != 0:
        for j in range(i+i, 1001, i):
            prime_number[j] = 0

for i in input_number:
    if prime_number[i] != 0:
        result += 1

print(result)

m = int(input())
n = int(input())

prime_number = [i for i in range(0, 10001)]
prime_number[1] = 0
result = 0
min_num = 99999

for i in range(2, int(10000 ** 0.5)):
    if prime_number[i] != 0:
        for j in range(i+i, 10001, i):
            prime_number[j] = 0

for i in range(m, n+1):
    if prime_number[i] != 0:
        result += prime_number[i]

        if prime_number[i] < min_num:
            min_num = prime_number[i]

if result == 0:
    print(-1)
else:
    print(result)
    print(min_num)
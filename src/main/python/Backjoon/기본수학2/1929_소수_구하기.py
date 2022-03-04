a, b = map(int, input().split())
primeNumber = [i for i in range(b+1)]

primeNumber[1] = 0

# 에라토스테네스의 체
for i in range(2, int(b**0.5)+1) :
    if primeNumber[i] != 0 :
        for j in range(i+i, b+1, i) :
            primeNumber[j] = 0

for i in range(a, b+1) :
    if primeNumber[i] != 0 :
        print(i)
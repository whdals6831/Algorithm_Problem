import sys

length = 123456*2+1
primeNumber = [i for i in range(length)]
primeNumber[1] = 0

for i in range(2, int(length**0.5)):
    if primeNumber[i] != 0:
        for j in range(i+i, length, i):
            primeNumber[j] = 0

testCase = int(sys.stdin.readline())

while testCase != 0:
    answer = 0

    for n in primeNumber[testCase+1:testCase*2+1]:
        if n != 0:
            answer += 1

    print(answer)
    testCase = int(sys.stdin.readline())
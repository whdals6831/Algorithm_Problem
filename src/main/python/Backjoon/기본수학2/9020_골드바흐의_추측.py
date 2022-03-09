import sys

testCase = int(input())
primeNumber = [i for i in range(10001)]
primeNumber[1] = 0

for i in range(2, int(10001**0.5)):
    if primeNumber[i] != 0:
        for j in range(i+i, 10001, i):
            primeNumber[j] = 0

def getPartition(n):
    for i in range(n//2+1, 1, -1):
            if primeNumber[i] != 0:
                for j in range(n//2, n):
                    
                    if primeNumber[j] == 0 :
                        continue

                    if (i+j) == n:
                        print(i, j)
                        return

for _ in range(testCase):
    n = int(sys.stdin.readline())
    getPartition(n)
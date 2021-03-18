# 완전탐색의 유연한 생각
import sys
from itertools import combinations

n, k = map(int, sys.stdin.readline().split())

alphabet = [[0]*26 for i in range(n)]
ans = 0

antatica = ['a', 'n', 'c', 't', 'i']

teach_count = k - 5
words = []

for _ in range(n):
    words.append(sys.stdin.readline().rstrip()[4:-4])

for i, v in enumerate(words):
    for j in set(v):
        if j not in antatica:
            alphabet[i][ord(j)-97] += 1

for i in alphabet:
    print(i)


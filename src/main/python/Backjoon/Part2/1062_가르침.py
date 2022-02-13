# 완전탐색의 유연한 생각
import sys
from itertools import combinations

n, k = map(int, sys.stdin.readline().split())

bit_masking_words = [0] * n
words = []
ans = 0

for i in range(n):
    temp = sys.stdin.readline().rstrip()

    for j in temp:
        # |= 는 논리합을 의미하며 OR 연산을 한 결과를 왼쪽 변수에 저장
        # << 는 왼쪽 값을 오른쪽 값만큼 bit를 왼쪽으로 이동시키는 건데 
        # 2**n 라고 생각하면된다.
        # 결과값은 이진수를 정수로 변환한 값이 저장된다.
        # 결국 각 알파벳 별로 비트마스킹됨 
        # ex) an = 8193
        bit_masking_words[i] |= (1 << (ord(j) - ord('a')))
        words.append(j)

if k < 5:
    print(0)
else:
    antatica = ['a', 'c', 't', 'i', 'n']
    # antatica를 뺀 나머지 알파벳
    remain_alpha = set(words) - set(antatica)

    # 남아있는 알파벳이 배울 수 있는 문자 개수보다 작을 경우 n을 출력
    if len(remain_alpha) <= k-5 :
        print(n)
    else :
        # remain_alpha에서 k-5만큼 조합하는 모든 경우의 수
        # 모든 경우의 수의 단어를 비교
        for i in list(combinations(remain_alpha, k-5)):
            each = 0
            result = 0

            # |= 연산은 단어 배우기, & 연산은 단어를 읽을 수 있는지를 체크
            # antatica 문자를 비트마스킹해서 each를 학습
            for j in antatica:
                each |= (1 << (ord(j) - ord('a')))
            # 추가로 경우의 수 하나도 학습
            for j in i:
                each |= (1 << (ord(j) - ord('a')))

            # antatica와 경우의 수 1개를 학습한 each와 대조
            # 입력된 단어 중 포함되어 있는 수가 가장 많으면 ans에 대입
            for j in bit_masking_words:
                if each & j == j:
                    result += 1

            ans = max(ans, result)

        print(ans)
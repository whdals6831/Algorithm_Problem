s = list(input())
p = list(input())

def makeLPS(p):
    j = 0 # s와 p가 최대한 겹치는 인덱스
    lps = [0]*len(p)
    
    for i in range (1, len(p)):
        while j > 0 and p[i] != p[j]:
            # 전에 있던 인덱스를 찾아가 겹쳐진게 있었으면 그곳에서부터 다시시작
            # 앞에 인덱스들은 겹쳐지는게 보장이 됨
            j = lps[j-1]

        if p[i] == p[j]:
            j += 1
            lps[i] = j
    return lps


# KMP 알고리즘!!
def KMP(s, p):
    lps = makeLPS(p)
    j = 0

    for i in range(len(s)):
        while j>0 and s[i] != p[j]:
            j = lps[j-1]

        if s[i] == p[j]:
            if j == len(p)-1:
                return True
            else:
                j += 1
    
    return False


isAnswer = KMP(s, p)

if isAnswer:
    print(1)
else:
    print(0)
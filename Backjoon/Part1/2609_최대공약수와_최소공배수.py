# GCD는 최대공약수 -> 유클리드 호제법 사용
# GCM은 최소공배수
import sys 
sys.setrecursionlimit(10**6) # 재귀 깊이를 늘려줌

a, b = map(int, input().split())

def GCD(a, b): # a >= b
    return GCD(b, a % b) if b else a

def GCM(a, b, original_a, original_b):
    if a > b:
        return GCM(a, b+original_b, original_a, original_b)
    elif a < b:
        return GCM(a+original_a, b, original_a, original_b)
    else:
        return a

if a > b:
    print(GCD(a, b))
else:
    print(GCD(b, a))

print(GCM(a, b, a, b))
tase_case = int(input())

for _ in range(0, tase_case):
    a = list(map(int, input().split()))
    sorted_a = sorted(a)
    print(sorted_a[-3])
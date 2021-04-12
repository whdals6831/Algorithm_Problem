n, s, m = map(int, input().split())
v = list(map(int, input().split()))
volume = [[] for _ in range(n+1)]
volume[0].append(s)
isAnswer = True

for i, k in enumerate(v):
    for j in volume[i]:
        if j+k <=m:
            volume[i+1].append(j+k)
        if j-k >=0:
            volume[i+1].append(j-k)
    # 중복 제거가 핵심!!
    volume[i+1] = list(set(volume[i+1]))
    
    if len(volume[i+1]) == 0:
        isAnswer = False
        break

if isAnswer:
    print(max(volume[n]))
else:
    print(-1)
s = int(input())

emo = [float('inf')]*1001
emo[1] = 0

for i in range(1, 1000):
    for j in range(i+1, 1001):
        if j == i*2: # 배수의 처음은 클립보드에 저장해야되기 때문에 +2를 한다.
            emo[j] = min(emo[i]+2, emo[j])
        elif j%i == 0: # 다음 배수부터는 몫만큼 시간을 더해준다.
            emo[j] = min(emo[i]+j//i, emo[j])
        
        # 직전의 이모티콘의 개수에서 걸리는 시간이 현재 시간의 +1보다 크면 
        # 현재 시간의 +1로 바꿔줌 
        if emo[j-1] > emo[j]+1:
            emo[j-1] = emo[j]+1

print(emo[s])
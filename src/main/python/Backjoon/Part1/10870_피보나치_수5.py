n = int(input())

fivonacci = [0, 1]

if n == 0:
    print(fivonacci[0])
elif n == 1:
    print(fivonacci[1])
else :
    for i in range(2, n+1):
        fivonacci.append(fivonacci[i-1] + fivonacci[i-2])
    print(fivonacci[-1])
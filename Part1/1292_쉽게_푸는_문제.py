a, b = map(int, input().split())

numbers = [i for i in range(1, 50) for _ in range(i)]

result = 0

for i in range(a-1, b):
    result += numbers[i]

print(result)
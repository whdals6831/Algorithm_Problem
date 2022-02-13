def get_binary_index(n):
    binary_number = []

    while n >= 2:
        binary_number.append(n%2)
        n = n // 2
    binary_number.append(n)

    answer = ''

    for i, v in enumerate(binary_number):
        if v == 1:
            answer = answer + f'{i} '
        
    return answer

t = int(input())

for _ in range(0, t):
    n = int(input())
    
    print(get_binary_index(n))
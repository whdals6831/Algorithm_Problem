# prices	return
# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]

def solution(prices):
    answer = []
    
    for i, price in enumerate(prices):
        second = 0
        for j in range(i+1, len(prices)):
            if prices[j] >= price:
                second += 1
            else:
                second += 1
                break
        answer.append(second)
    
    return answer
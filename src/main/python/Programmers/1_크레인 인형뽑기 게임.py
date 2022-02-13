# board	moves	result
# [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	[1,5,3,5,1,2,1,4]	4

import numpy as np

def solution(board, moves):
    answer = 0
    basket = []
    moved = False
    
    for x in moves:
        moved = False
        for y in range(len(board)):
            if board[y][x-1] != 0 and not moved:
                basket.append(board[y][x-1])
                board[y][x-1] = 0
                moved = True
                
                if len(basket) > 1 and (basket[-1] == basket[-2]):
                    answer += 2
                    basket.pop()
                    basket.pop()
                    
    return answer
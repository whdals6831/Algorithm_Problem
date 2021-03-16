# name	return
# JEROEN	56
# JAN	23

name = "JAN"

def min_movement(name):
    if 'A' in name:
        start_idx = 0
        end_idx = 0
        sequence = 0
        max_idx = [0, 0]

        for i,d in enumerate(name):
            # if i != 0:
            if d == 'A' and sequence == 1:
                end_idx += 1
                if max_idx[1] - max_idx[0] < end_idx - start_idx:
                    max_idx[0] = start_idx
                    max_idx[1] = end_idx

            elif d == 'A' and sequence == 0:
                start_idx = i
                end_idx = i+1
                sequence = 1

            else :
                sequence = 0
                if max_idx[1] - max_idx[0] < end_idx - start_idx:
                    max_idx[0] = start_idx
                    max_idx[1] = end_idx
        

        if max_idx[1] == len(name):
            return max_idx[0]-1
        elif max_idx[0] == 0:
            return len(name) - max_idx[1]
        elif max_idx[1] - max_idx[0] >= max_idx[0]:
            if max_idx[0] <= len(name) - max_idx[1]:
                return (max_idx[0]-1)*2 + len(name) - max_idx[1] # EEAAAAAEEEE
            else:
                return max_idx[0]-1 + (len(name) - max_idx[1])*2 # EEEEAAAAAAEE
        else :
            return len(name)-1
    else:
        return len(name)-1

def solution(name):
    answer = 0
    
    for i in name:
        if (ord(i)-65) < 13:
            answer += ord(i)-65
        else:
            answer += 91 - ord(i)
    answer += min_movement(name)

    return answer

if __name__ == "__main__":
    print(solution(name))


# def solution(name): # 똑똑한 방법
#     answer, n = 0, len(name) 
#     move = n - 1

#     for i in range(n):
#         answer += min(ord(name[i]) - ord('A'), abs(ord(name[i]) - ord('Z') - 1))

#         next = i + 1
#         while next < n and name[next] == 'A':
#             next += 1

#         move = min(move, i + n - next + min (i, n - next))

#     return answer + move
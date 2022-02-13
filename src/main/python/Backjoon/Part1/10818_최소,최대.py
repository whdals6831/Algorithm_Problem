n = int(input())
n_list = map(int, input().split())

sorted_n_lit = sorted(n_list)

print(sorted_n_lit[0], sorted_n_lit[-1])
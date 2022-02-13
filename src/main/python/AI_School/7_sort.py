# 삽입, 선택, 버블로 구현

def insert_sort(num_list) :

    for i in range(len(num_list)) :
        now_index = i
        search_index = i - 1
        
        for _ in range(i) :
            if num_list[search_index] > num_list[now_index] :
                temp = num_list[search_index]
                num_list[search_index] = num_list[now_index]
                num_list[now_index] = temp
                now_index -= 1
                search_index -= 1
            else :
                break
    
    print(num_list)



def selection_sort(num_list) :
    for i in range(len(num_list)) :
        min_index = i

        for j in range(i+1, len(num_list)) :
            if num_list[j] < num_list[min_index]:
                min_index = j

        # temp = num_list[i]
        # num_list[i] = num_list[min_index]
        # num_list[min_index] = temp

        # 더 쉽게 값을 교환하는 법
        num_list[i], num_list[min_index] = num_list[min_index], num_list[i]
    
    print(num_list)
            


def bubble_sort(num_list) :
    for i in range(len(num_list)) :
        swap_check_flag = False
        for j in range(i+1, len(num_list)) :
            swap_check_flag = True
            if num_list[j-1] > num_list[j] :
                num_list[j-1], num_list[j] = num_list[j], num_list[j-1]
        
        if not swap_check_flag:
            break
    
    print(num_list)


def main() :
    n = int(input())

    num_list = []

    for _ in range(n) :
        value = int(input())
        num_list.append(value)

    insert_sort(num_list)
    selection_sort(num_list)
    bubble_sort(num_list)

main()

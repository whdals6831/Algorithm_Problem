# ##### 반복문 풀이방법 #####
# n, k = map(int, input().split())

# num_list = [i for i in range(1, n+1)]
# # num_list = list(range(1, n+1))

# idx = k-1

# print("<", end="")
# while len(num_list) > 1 :
#     print(num_list.pop(idx), end= ", ")
#     idx += k-1
#     idx %= len(num_list)
    
# print(f"{num_list.pop(idx)}>")


# ##### 덱 풀이방법 #####
# from collections import deque

# n, k = map(int, input().split())
# num_list = deque(range(1, n+1))

# result_str = ""
# while len(num_list) > 0 :
#     num_list.rotate(-(k-1))
#     result_str += f"{num_list.popleft()}, "

# print(f"<{result_str.rstrip(', ')}>")



##### 연결리스트 풀이방법 #####
class LinkedList:
    class Node:
        def __init__(self, data, link=None):
            self.data = data
            self.next_node = link
    
    def __init__(self):
        self.size = 0
        self.head_node = None
        self.tail_node = None

    def empty(self):
        return self.size == 0

    def append(self, data):
        before_node = self.tail_node
        new_node = self.Node(data)

        if self.empty():
            self.head_node = new_node
            new_node.next_node = new_node
        else:
            new_node.next_node = before_node.next_node
            before_node.next_node = new_node

        self.size += 1
        self.tail_node = new_node

    def pop(self, before_node):
        if not self.empty():
            target_node = before_node.next_node
            before_node.next_node = target_node.next_node

            if self.head_node.data == target_node.data:
                self.head_node = target_node.next_node
            if self.tail_node.data == target_node.data:
                self.tail_node = before_node

            self.size -= 1

            if self.empty():
                self.head_node = None
                self.tail_node = None

            return target_node.data

n, k = map(int, input().split())

llist = LinkedList()
for i in range(1, n+1):
    llist.append(i)

current_node = llist.tail_node
result_list = []

while not llist.empty():
    for _ in range(k-1):
        current_node = current_node.next_node

    result_list.append(str(llist.pop(current_node)))

print(f"<{', '.join(result_list)}>")
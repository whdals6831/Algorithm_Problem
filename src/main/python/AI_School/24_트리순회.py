# 7
# A B C
# B D .
# C E F
# E . .
# F . G
# D . .
# G . .

# class Node:
#         def __init__(self, data, left=None, right=None) :
#             self.data = data
#             self.left_node = left
#             self.right_node = right

# class BinaryTree:
#     def __init__(self, root_node=None):
#         self.root_node = root_node
    
#     def preorder(self, node):

#         if node is None:
#             return

#         print(node.data, end = "")
#         self.preorder(node.left_node)
#         self.preorder(node.right_node)

#     def inorder(self, node):

#         if node is None:
#             return

#         self.inorder(node.left_node)
#         print(node.data, end = "")
#         self.inorder(node.right_node)

#     def postorder(self, node):

#         if node is None:
#             return

#         self.postorder(node.left_node)
#         self.postorder(node.right_node)
#         print(node.data, end = "")

# n = int(input())
# temp_dict = {}

# for _ in range(n):
#     root_data, left_data, right_data = input().split()
#     new_node = Node(root_data)

#     temp_dict[left_data] = [new_node, "left"]
#     temp_dict[right_data] = [new_node, "right"]

#     if root_data == 'A':
#         tree = BinaryTree(new_node)
#     else :
#         if temp_dict[root_data][1] == "left":
#             temp_dict[root_data][0].left_node = new_node
#         elif temp_dict[root_data][1] == "right":
#             temp_dict[root_data][0].right_node = new_node

# tree.preorder(tree.root_node)
# print()
# tree.inorder(tree.root_node)
# print()
# tree.postorder(tree.root_node)




def preorder(node, node_list):
    if node == '.':
        return

    left = node_list[node][0]
    right = node_list[node][1]

    print(node, end="")
    preorder(left, node_list)
    preorder(right, node_list)


def inorder(node, node_list):
    if node == '.':
        return

    left = node_list[node][0]
    right = node_list[node][1]

    inorder(left, node_list)
    print(node, end="")
    inorder(right, node_list)


def postorder(node, node_list):
    if node == '.':
        return

    left = node_list[node][0]
    right = node_list[node][1]

    postorder(left, node_list)
    postorder(right, node_list)
    print(node, end="")


n = int(input())
node_list = {}

for _ in range(n):
    root, left, right = input().split()
    node_list[root] = [left, right]


preorder('A', node_list)
print()
inorder('A', node_list)
print()
postorder('A', node_list)

    # {
    #     'A' : ['B','C'],
    #     'B' : ['D','.'],
    # }

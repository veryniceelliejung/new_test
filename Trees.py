# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.right_child = None
#         self.left_child = None
#
#
# a = Node("root node-a")
# b = Node("left child node-b")
# c = Node("right child node-c")
# d = Node("left left grandchild node-d")
# e = Node("left right grandchild node-e")
# f = Node("right right grandchild node-f")
# g = Node("left left grandgrandchild node-g")
# h = Node("left right grandgrandchild node-h")
#
# a.left_child = b
# a.right_child = c
# b.left_child = d
# b.right_child = e
# c.right_child = f
# d.left_child = g
# d.right_child = h
#
#
#
# # current = n1
# # while current:
# #     print(current.data)
# #     current = current.left_child
#
# def inorder(root_node):
#     current = root_node
#     if current is None:
#         return
#     inorder(current.left_child)
#     print(current.data)
#     inorder(current.right_child)
#
# def preorder(root_node):
#     current = root_node
#     if current is None:
#         return
#     print(current.data)
#     preorder(current.left_child)
#     preorder(current.right_child)
#
# def postorder(root_node):
#     current = root_node
#     if current is None:
#         return
#     postorder(current.left_child)
#     postorder(current.right_child)
#     print(current.data)
#
# postorder(a)

# Level-order traversal
from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

n1 = Node("root node")
n2 = Node("left child node")
n3 = Node("right child node")
n4 = Node("left grandchild node")

n1.left_child = n2
n1.right_child = n3
n2.left_child = n4

def level_order_traversal(root_node):
    list_of_nodes = []
    traversal_queue = deque([root_node])
    while len(traversal_queue) > 0:
        node = traversal_queue.popleft()
        list_of_nodes.append(node.data)
        if node.left_child:
            traversal_queue.append(node.left_child)
            if node.right_child:
                traversal_queue.append(node.right_child)
    return list_of_nodes

print(level_order_traversal(n1))

# Expression trees
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class Stack:
    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)
    def pop(self):
        return self.elements.pop()

expr = "4 5 + 5 3 - *".split()
stack = Stack()

for term in expr:
    if term in "+-*/":
        node = TreeNode(term)
        node.right = stack.pop()
        node.left = stack.pop()
    else:
        node = TreeNode(int(term))
    stack.push(node)

def calc(node):
    if node.data == "+":
        return calc(node.left) + calc(node.right)
    elif node.data == "-":
        return calc(node.left) - calc(node.right)
    elif node.data == "*":
        return calc(node.left) * calc(node.right)
    elif node.data == "/":
        return calc(node.left) / calc(node.right)
    else:
        return node.data

root = stack.pop()
result = calc(root)
print(result)
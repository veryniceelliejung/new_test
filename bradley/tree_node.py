# class TreeNode:
#
#     def __init__(self, value):
#         self.left = None
#         self.right = None
#         self.value = value
#         self.content = None
#
#     def insert(self, value, content=None):
#         if value < self.value:
#             if self.left is None:
#                 self.left = TreeNode(value)
#                 self.left.content = content
#             else:
#                 self.left.insert(value, content)
#
#         else:
#             if self.right is None:
#                 self.right = TreeNode(value)
#                 self.right.content = content
#             else:
#                 self.right.insert(value, content)
#
#     def inorder_traversal(self):
#         if self.left:
#             self.left.inorder_traversal()
#         print(self.value)
#         if self.right:
#             self.right.inorder_traversal()
#
#     def preorder_traversal(self):
#         print(self.value)
#         if self.left:
#             self.left.preorder_traversal()
#         if self.right:
#             self.right.preorder_traversal()
#
#     def postorder_traversal(self):
#         if self.left:
#             self.left.postorder_traversal()
#         if self.right:
#             self.right.postorder_traversal()
#         print(self.value)
#
#     def find(self, value):
#         if value < self.value:
#             if self.left is None:
#                 return None
#             else:
#                 return self.left.find(value)
#         elif value > self.value:
#             if self.value is None:
#                 return None
#             else:
#                 return self.right.find(value)
#         else:
#             return self
#
# tree = TreeNode(6)
# tree.insert(5)
# tree.insert(2)
# tree.insert(4)
# tree.insert(1)
# tree.insert(2)
# tree.insert(4)
# tree.insert(19, {'data': 'Hello World'})
# tree.insert(29)
# tree.insert(11)
# tree.insert(4)
# tree.insert(2)
#
# # tree.postorder_traversal()
# print(tree.find(19).content['data'])

class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child
    def has_right_child(self):
        return self.right_child
    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent
    def is_leaf(self):
        return not (self.right_child or self.left_child)
    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1
    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)

    def __setitem__(self, k, v):
        self.put(k, v)
    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False
    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def find_successor(self):
        succ = None
        if self.has_right_child():
            succ = self.right_child.find_min()
        else:
            if self.parent():
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self
        return succ

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parnet.right_child = None

        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent

            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def remove(self, current_node):
        if current_node.is_leaf():
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_both_children():
            succ = current_node.find_successor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.payload = succ.payload
        else:
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_node_data(current_node.left_child.key, current_node.left_child.payload,
                                                   current_node.left_child.left_child, current_node.left_child.right_child)
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_node_data(current_node.right_child.key, current_node.right_child.payload,
                                                   current_node.right_child.left_child, current_node.right_child.right_child)

my_tree = BinarySearchTree()
my_tree[3] = 'red'
my_tree[4] = 'blue'
my_tree[6] = 'yellow'
my_tree[2] = 'at'

print(my_tree[6])
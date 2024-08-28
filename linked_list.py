#array는 big data일 경우 delete나 insert하기 어려움
#linked list는 이런면에서 유리함 non-contiguous, data and pointer

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def length(self):
        current = self.head
        total = 0
        while current.next != None:
            total += 1
            current = current.next
        return total

    def display(self):
        elems = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elems.append(current_node.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("Error: 'Get' Index out of range!")
            return None
        current_idx = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_idx == index:
                return current_node.data
            current_idx += 1

    def erase(self, index):
        if index >= self.length():
            print("Error: 'Erase' Index out of range!")
            return
        current_idx = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_idx == index:
                last_node.next = current_node.next #erasing current node
                return
            current_idx += 1



my_list = SinglyLinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()
my_list.erase(2)
my_list.display()

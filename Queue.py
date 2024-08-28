# class ListQueue:
#     def __init__(self):
#         self.items = []
#         self.front = self.rear = 0
#         self.size = 3
#
#     def enqueue(self, data):
#         if self.size == self.rear:
#             print("\n Queue is full")
#         else:
#             self.items.append(data)
#             self.rear += 1
#
#     def dequeue(self):
#         if self.front == self.rear:
#             print("Queue is empty")
#         else:
#             data = self.items.pop(0)
#             self.rear -= 1
#             return data


class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        new_node = Node(data, None, None)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def dequeue(self):
        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.prev
            self.head.prev = None
        elif self.count < 1:
            print("Queue is empty")
        self.count -= 1
        



q = ListQueue()
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print(q.items)
data = q.dequeue()
print(data)
print(q.items)
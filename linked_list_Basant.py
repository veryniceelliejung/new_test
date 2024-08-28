# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#
#
#
# # class SinglyLinkedList:
# #     def __init__(self):
# #         self.head = None
# #         self.size = 0
# #
# #     def append(self, data):
# #         node = Node(data)
# #         if self.head == None:
# #             self.head = node
# #         else:
# #             current = self.head
# #             while current.next:
# #                 current = current.next
# #             current.next = node
#
# # class SinglyLinkedList:
# #     def __init__(self):
# #         self.head = None
# #         self.tail = None
# #         self.size = 0
# #
# #     def append(self, data):
# #         node = Node(data)
# #         if self.tail:
# #             self.tail.next = node
# #             self.tail = node
# #
# #         else:
# #             self.head = node
# #             self.tail = node
#
#
# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0
#
#     def iter(self):
#         current = self.head
#         while current:
#             val = current.data
#             current = current.next
#             yield val
#     def append(self, data):
#         node = Node(data)
#         if self.head == None:
#             self.head = node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = node
#
#     def append_at_a_location(self, data, index): #좀 이상함
#         current = self.head
#         prev = self.head
#         node = Node(data)
#         count = 1
#
#         while current:
#             if count == 1:
#                 node.next = current
#                 self.head = node
#                 return
#
#             elif index == index:
#                 node.next = current
#                 prev.next = node
#                 return
#                 count += 1
#                 prev = current
#                 current = current.next
#
#             if count < index:
#                 print("The list has less number of elements")
#     def search(self, data):
#         for node in self.iter():
#             if data == node:
#                 return True
#             return False
#
#     def size(self):
#         count = 0
#         current = self.head
#         while current:
#             count += 1
#             current = current.next
#         return count
#
#     def delete_first_node(self):
#         current = self.head
#         if self.head is None:
#             print("No data element to delete")
#         elif current == self.head:
#             self.head = current.next
#
#
#     def delete_last_node(self):
#         current = self.head
#         prev = self.head
#         while current:
#             if current.next is None:
#                 prev.next = current.next
#                 self.size -= 1
#             prev = current
#             current = current.next
#
#     def delete(self, data):
#         current = self.head
#         prev = self.head
#         while current:
#             if current.data == data:
#                 if current == self.head:
#                     self.head = current.next
#                 else:
#                     prev.next = current.next
#                 self.size -= 1
#                 return
#             prev = current
#             current = current.next
#
#
# words = SinglyLinkedList()
# words.append('egg')
# words.append('ham')
# words.append('spam')
#
#
# current = words.head
# while current:
#     print(current.data)
#     current = current.next
#
#
# # words.append_at_a_location('new', 3)
# # current = words.head
# # while current:
# #     print(current.data)
# #     current = current.next
#
# # print(words.search('ham'))
#
# words.delete("ham")
# current = words.head
# while current:
#     print(current.data)
#     current = current.next


#Doubly linked lists
# class Node:
#     def __init__(self, data=None, next=None, prev=None):
#         self.data = data
#         self.next = next
#         self.prev = prev
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.count = 0
#
#     def append(self, data):
#         new_node = Node(data, None, None)
#         if self.head is None:
#             self.head = new_node
#             self.tail = self.head
#
#         else:
#             new_node.prev = self.tail
#             self.tail.next = new_node
#             self.tail = new_node
#
#         self.count += 1
#
#     def append_at_start(self, data):
#         new_node = Node(data, None, None)
#         if self.head is None:
#             self.head = new_node
#             self.tail = self.head
#
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
#         self.count += 1
#
#     def append_at_a_location(self, data):
#         current = self.head
#         prev = self.head
#         new_node = Node(data, None, None)
#         while current:
#             if current.data == data:
#                 new_node.prev = prev
#                 new_node.next = current
#                 prev.next = new_node
#                 current.prev = new_node
#                 self.count += 1
#             prev = current
#             current = current.next
#
#     def iter(self):
#         current = self.head
#         while current:
#             val = current.data
#             current = current.next
#             yield val
#
#     def contains(self, data):
#         for node_data in self.iter():
#             if data == node_data:
#                 print("Data item is present in the list.")
#                 return
#         print("Data item is not present in the list")
#         return
#
#     def delete(self, data):
#         current = self.head
#         node_deleted = False
#         if current is None:
#             print("List is empty.")
#         elif current.data == data:
#             self.head.prev = None
#             node_deleted = True
#             self.head = current.next
#         elif self.tail.data == data:
#             self.tail = self.tail.prev
#             self.tail.next = None
#             node_deleted = True
#         else:
#             while current:
#                 if current.data == data:
#                     current.prev.next = current.next
#                     current.next.prev = current.prev
#                     node_deleted = True
#                 current = current.next
#             if node_deleted == False:
#                 print("Item not found")
#         if node_deleted:
#             self.count -= 1
#
#
# words = DoublyLinkedList()
# words.append('egg')
# words.append('ham')
# words.append('spam')
#
# words.append_at_a_location("ham")
#
# print("Doubly linked list after adding an element after word 'ham' in the list.")
# current = words.head
# while current:
#     print(current.data)
#     current = current.next
#
# words.delete('ham')
# current = words.head
# while current:
#     print(current.data)
#     current = current.next


# Circular lists
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class CircularList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
            node.next = self.head
        else:
            self.head = node
            self.tail = node
            self.tail.next = self.tail
        self.size += 1

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.head
        prev = self.head
        while prev == current or prev != self.tail:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    self.tail.next = self.head
                elif current == self.tail:
                    self.tail = prev
                    prev.next = self.head
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next
            # if flag is False:
            #     print("Item not present in the list")



words = CircularList()
words.append('egg')
words.append('ham')
words.append('spam')
words.append('foo')
words.append('bar')

print("Let us try to delete something that isn't in the list")
words.delete('socks')
counter = 0
for word in words.iter():
    print(word)
    counter += 1
    if counter > 4:
        break
print()
print("Let us try to delete something that is in the list")
words.delete('foo')
counter = 0
for word in words.iter():
    print(word)
    counter += 1
    if counter > 3:
        break
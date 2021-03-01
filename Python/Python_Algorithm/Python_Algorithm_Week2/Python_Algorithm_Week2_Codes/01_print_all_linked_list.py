class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    def print_all(self):
        cur = self.head
        while cur.next is not None:
            print(cur.data)
            cur = cur.next

node = Node(3);
print(node)
print(node.data)
print(node.next)
print()

first_node = Node(4);
node.next = first_node
print(node)
print(node.data)
print(node.next)
print()
print(first_node)
print(first_node.data)
print(first_node.next)
print()
print(LinkedList.head.next)
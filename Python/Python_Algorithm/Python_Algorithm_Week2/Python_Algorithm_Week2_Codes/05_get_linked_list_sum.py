class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)


def get_linked_list_sum(linked_list_1, linked_list_2):
    '''
    node = linked_list_1.head
    sum1 = 0
    while node is not None:
        sum1 = (sum1 * 10) + node.data
        node = node.next

    node = linked_list_2.head
    sum2 = 0
    while node is not None:
        sum2 = sum2 * 10 + node.data
        node = node.next

    print(sum1)
    print(sum2)
    '''

    sum1 = _get_linked_list_sum(linked_list_1)
    sum2 = _get_linked_list_sum(linked_list_2)

    return sum1+sum2

def _get_linked_list_sum(linked_list):
    head = linked_list.head
    linked_list_sum = 0
    while head is not None:
        linked_list_sum = linked_list_sum * 10 + head.data
        head = head.next

    return linked_list_sum


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
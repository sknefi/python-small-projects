class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next

        curr_node.next = new_node

class Tests:
    def __init__(self):
        self.linked_list = LinkedList()

    def printLinkedList(self):
        for x in self.linked_list:
            print(x, end=' -> ')

        print('NULL')

    def test_append(self):
        self.linked_list.append('a')
        self.linked_list.append('b')
        self.linked_list.append('c')
        self.linked_list.append('d')

        self.printLinkedList()


test = Tests()
test.test_append()
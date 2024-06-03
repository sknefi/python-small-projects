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

    def create_new(self, *args):
        # creates new linked list, with new head
        # so linked list will contain only values in *args
        if not args:
            print('create_new: Any args set, doing nothing')
            return None

        head = Node(args[0])
        current = head
        self.head = head

        for value in args[1:]:
            current.next = Node(value)
            current = current.next

        print('create_new: Created whole new linked list')
        return head

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            print(f'append: Append value {value} as head of LinkedList')
            return

        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next

        curr_node.next = new_node
        print(f'append: Append value {value} on the end of LinkedList')

    def remove_value(self, value):
        if self.head is None:
            print('remove_value: LinkedList is empty')

            return False

        prev_node = None
        curr_node = self.head

        while curr_node:
            if curr_node.value == value:
                if prev_node:
                    print(f'remove_value: Removed node with value {value} from LinkedList')
                    prev_node.next = curr_node.next
                else:
                    print(f'remove_value: Removed head node with value {value} from LinkedList')
                    self.head = curr_node.next

                return True

            prev_node = curr_node
            curr_node = curr_node.next

        print(f"remove_value: Value '{value}' not found in LinkedList")
        return False

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print(f'prepend: Prepend value {value} as head of LinkedList')
            return

        new_node.next = self.head
        self.head = new_node
        print(f'prepend: Prepend value {value} at the beginning of LinkedList (new head)')

    def remove_last(self):
        if self.head is None:
            print('remove_last: LinkedList is empty')
            return False

        if self.head.next is None:
            print(f'remove_last: Removed last node with value {self.head.value} from LinkedList')
            self.head = None
            return True

        prev_node = None
        curr_node = self.head
        while curr_node.next:
            prev_node = curr_node
            curr_node = curr_node.next

        prev_node.next = None
        print(f'remove_last: Removed last node with value {curr_node.value} from LinkedList')
        return True


class Tests:
    def __init__(self):
        self.linked_list = LinkedList()
        self.helper_list = LinkedList()  # this list will be empty all the time

    def printLinkedList(self):
        for x in self.linked_list:
            print(x, end=' -> ')

        print('NULL')
        print()

    def printHelperList(self):
        for x in self.helper_list:
            print(x, end=' -> ')

        print('NULL')
        print()

    def test_append(self):
        print('===APPEND===')

        print("Adding value 'a' to LinkedList")
        self.linked_list.append('a')
        self.printLinkedList()

        print("Adding value 'b' to LinkedList")
        self.linked_list.append('b')
        self.printLinkedList()

        print("Adding value 'c' to LinkedList")
        self.linked_list.append('c')
        self.printLinkedList()

        print("Adding value 'd' to LinkedList")
        self.linked_list.append('d')
        self.printLinkedList()

    def test_remove(self):
        print('===REMOVE===')

        print("Removing value 'b' from the linked list:")
        self.linked_list.remove_value('b')
        self.printLinkedList()

        print("Removing value 'a' from the linked list:")
        self.linked_list.remove_value('a')
        self.printLinkedList()

        print("Removing value 'd' from the linked list:")
        self.linked_list.remove_value('d')
        self.printLinkedList()

        print("Removing value 'x' (not in the list) from the linked list:")
        self.linked_list.remove_value('x')
        self.printLinkedList()

    def test_create_linked_list(self):
        print('===CREATE NEW LINKED LIST===')
        print("Creating linked list from parameters 1, 2, 3, 4, 5:")
        self.linked_list.create_new(1, 2, 3, 4, 5)
        self.printLinkedList()

        print("Creating linked list from parameters 'a', 'b', 'c':")
        self.linked_list.create_new('a', 'b', 'c')
        self.printLinkedList()

        print("Creating linked list from empty parameters:")
        self.linked_list.create_new()
        self.printLinkedList()

    def test_prepend(self):
        print('===PREPEND===')

        print("Prepending value 'x' to LinkedList")
        self.linked_list.prepend('x')
        self.printLinkedList()

        self.helper_list = LinkedList()
        print("Prepending value 'y' to LinkedList")
        self.helper_list.prepend('y')
        self.printHelperList()

    def test_remove_last(self):
        print('===REMOVE LAST===')

        print("Creating linked list from parameters 1, 2, 3, 4, 5:")
        self.linked_list.create_new(1, 2, 3, 4, 5)
        self.printLinkedList()

        print("Removing last element from the linked list:")
        self.linked_list.remove_last()
        self.printLinkedList()

        print("Removing last element from the linked list again:")
        self.linked_list.remove_last()
        self.printLinkedList()

        print("Removing last element from the linked list again:")
        self.linked_list.remove_last()
        self.printLinkedList()

        print("Removing last element from the linked list again:")
        self.linked_list.remove_last()
        self.printLinkedList()

        print("Removing last element from the linked list again:")
        self.linked_list.remove_last()
        self.printLinkedList()

        print("Trying to remove last element from an empty linked list:")
        self.linked_list.remove_last()

test = Tests()
test.test_append()
test.test_remove()
test.test_create_linked_list()
test.test_prepend()
test.test_remove_last()



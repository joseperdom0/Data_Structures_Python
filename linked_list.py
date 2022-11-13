# Linked List from scratch

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.__dict__)


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = new_node

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def printLinkedList(self):
        print_node = self.head
        while (print_node):
            print(print_node.value, end=" ")
            print_node = print_node.next

    def __str__(self):
        return str(self.__dict__)


my_linked_list = LinkedList()
print(my_linked_list)
my_linked_list.append(10)
print(my_linked_list)
my_linked_list.append(5)
my_linked_list.push(1)
my_linked_list.append(400)
my_linked_list.push(300)
my_linked_list.printLinkedList()

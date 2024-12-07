class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp_head = self.head
        while temp_head is not None:
            print(temp_head.value)
            temp_head = temp_head.next

    def append(self, value):
        new_node = Node(value=value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length = 1
        return True

    def pop(self):
        # Empty linked list
        if self.length == 0:
            print("Empty List")
            return None
        
        # Single node
        if self.length == 1:
            popped = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return popped

        # Multiple nodes
        temp_head = self.head
        while temp_head.next is self.tail:
            # Arrives second last
            temp_head = temp_head.next
        popped = self.tail  # Save the current tail
        self.tail = temp_head
        self.tail.next = None
        self.length -= 1
        return popped

    def prepend(self, value):
        pass

    def insert(self, index, value):
        pass


# linked_list = LinkedList(5)
# linked_list.append(6)
# linked_list.print_list()
# linked_list.pop()
# linked_list.print_list()

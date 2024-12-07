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
        '''
        Adds node to the last of the list
        '''
        new_node = Node(value=value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        '''
        Removes the last node and returns it, or returns None if the list is empty.
        '''
        # Case: Empty linked list
        if self.length == 0:
            print("Empty List")
            return None

        # Case: Single node in the list
        if self.length == 1:
            popped = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return popped

        # Case: Multiple nodes in the list
        temp = self.head
        while temp.next is not self.tail:  # Traverse to the second-to-last node
            temp = temp.next

        popped = self.tail  # Save the current tail
        self.tail = temp  # Update tail to the second-to-last node
        self.tail.next = None  # Disconnect the old tail
        self.length -= 1  # Decrease length
        return popped

    def prepend(self, value):
        '''
        Adds Item to the beginning of the list
        '''
        # Created new node
        new_node = Node(value)
        
        # If list is empty:
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # Non empty list
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1

    def insert(self, index, value):
        pass


linked_list = LinkedList(5)
linked_list.append(6)
linked_list.print_list()
print("pop")
linked_list.pop()
linked_list.print_list()
print("after pop")
linked_list.prepend(4)
linked_list.print_list()

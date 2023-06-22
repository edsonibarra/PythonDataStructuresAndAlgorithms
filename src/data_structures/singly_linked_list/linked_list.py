from node import Node


class LinkedList:
    EMPTY_LINKED_LIST_MSG = "Linked List is Empty"
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        It adds a new Node at the end of the linked list.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
    
    def print_list(self):
        """
        It prints each value in the linked list in a friendly way.
        """
        print("\n------ PRINTING LINKED LIST ------")
        if self.is_empty():
            print(LinkedList.EMPTY_LINKED_LIST_MSG)
            return
        current_node = self.head
        while current_node:
            print(f"[{current_node.data}]", end='->')
            current_node = current_node.next
        print("None")
    
    def prepend(self, data):
        """
        It adds a new Node at the beginning of the linked list.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        current_node = self.head
        new_node.next = current_node
        self.head = new_node

    def is_empty(self):
        """
        Verifies if the linked list is empty
        """
        return self.head is None


def main():
    ll = LinkedList()
    ll.print_list()

    # Insert nodes at the end of the linked list using append method
    values_to_add = [n for n in range(1, 7)]
    for value in values_to_add:
        ll.append(value)
    
    ll.print_list()

    # Insert nodes at the beginning of the linked list
    negative_values_to_add = [n * -1 for n in range(4)]
    for value in negative_values_to_add:
        ll.prepend(value)
    
    ll.print_list()


if __name__ == "__main__":
    main()

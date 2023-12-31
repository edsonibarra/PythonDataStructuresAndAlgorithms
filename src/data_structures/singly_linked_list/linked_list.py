from .node import Node


class LinkedList:
    EMPTY_LINKED_LIST_MSG = "Linked List is Empty"
    DELETE_FROM_EMPTY_LINKED_LIST_MSG = "Could not delete from empty linked list"
    NODE_NOT_FOUND = "Node with data = {} not found in {}"

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
            return LinkedList.EMPTY_LINKED_LIST_MSG
        current_node = self.head
        while current_node:
            print(f"[{current_node.data}]", end="->")
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

    def delete_node_by_value(self, value_to_delete):
        """
        Delete a node based on the value provided in
        value_to_delete argument
        """
        if self.is_empty():
            message = LinkedList.DELETE_FROM_EMPTY_LINKED_LIST_MSG
            print(message)
            return message

        current_node = self.head
        prev = None  # Previous Node
        # Check if the head node is the one to remove from linked list
        if current_node.data == value_to_delete:
            # If it is, update the head node to current_node.next and exit
            self.head = current_node.next
            current_node = None
            return

        # Traverse Linked list until node containing value_to_delete is found
        while current_node and current_node.data != value_to_delete:
            prev = current_node
            current_node = current_node.next

        # If current_node exists, it means the value_to_delete node exits within linked list
        if current_node:
            # Update the prev.next to point to current_node.next and remove current_node form linked list
            prev.next = current_node.next
            current_node = None
            return
        # If current_node does not exists it means value_to_delete was not found in the linked list
        else:
            message = LinkedList.NODE_NOT_FOUND.format(
                value_to_delete, "delete_node_by_value"
            )
            print(message)
            return message

    def delete_node_by_position(self, position_to_delete):
        """
        Deletes a node based on the position provided in position_to_delete
        """
        if self.is_empty():
            message = LinkedList.DELETE_FROM_EMPTY_LINKED_LIST_MSG
            print(message)
            return message
        current_node = self.head
        prev = None
        count = 0  # Keep track of the current position

        # Check if the node to delete is the head node
        # Delete node at position 0 when count is still 0.
        if position_to_delete == count:
            self.head = current_node.next
            current_node = None
            return

        while current_node and count != position_to_delete:
            count += 1
            current_node = current_node.next

        # If current_node exists, it means the value_to_delete node exits within linked list
        if current_node:
            # Update the prev.next to point to current_node.next and remove current_node form linked list
            prev.next = current_node.next
            current_node = None
            return
        # If current_node does not exists it means value_to_delete was not found in the linked list
        else:
            message = LinkedList.NODE_NOT_FOUND.format(
                position_to_delete, "delete_node_by_position"
            )
            print(message)
            return message

    def __len__(self):
        """
        Returns the length of the linked list
        """
        count = 0
        if self.is_empty():
            return count

        # Traverse the linked list and increase count with every node
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def reverse(self):
        """
        Transform the linked list into a reversed linked list
        Example:
        [1] -> [2] -> [3] -> None
        Result:
        [3] -> [2] -> [1] -> None
        """
        if self.is_empty():
            message = LinkedList.EMPTY_LINKED_LIST_MSG
            print(message)
            return message
        current_node = self.head
        prev = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node
        self.head = prev

    def remove_duplicates(self):
        """
        It deletes every duplicate node data in the linked list leaving just one node of each value
        """
        duplicate_values = {}
        current_node = self.head
        prev = None
        while current_node:
            if current_node.data in duplicate_values:
                prev.next = current_node.next
                current_node = None
            else:
                prev = current_node
                duplicate_values[current_node.data] = True
            current_node = prev.next

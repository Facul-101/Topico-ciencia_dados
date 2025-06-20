from my_singly_linked_list import SinglyLinkedList
from typing import Iterator, Self, Any, Optional
from nodes import TwoWaysNode


class DoublyLinkedList(SinglyLinkedList):

    def __init__(self) -> None:
        self.head: Optional[TwoWaysNode] = None
        self._size = 0

    def insert_beginning(self, value: Any):
        self._size += 1
        new_node = TwoWaysNode(value)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, value: Any):
        self._size += 1

        new_node = TwoWaysNode(value)

        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        for _ in range(self._size - 2):
            current_node: TwoWaysNode = current_node.next # type: ignore

        current_node.next = new_node
        new_node.previous = current_node
    
    def insert_by_index(self, value, index):
        self._valid_index(index)
        
        if index == 0:
            self.insert_beginning(value)
            return

        new_node = TwoWaysNode(value)

        previous_node: TwoWaysNode = self.head # type: ignore
        for _ in range(index - 1):
            previous_node = previous_node.next # type: ignore

        new_node.next = previous_node.next
        new_node.previous = previous_node
        previous_node.next = new_node
        new_node.next.previous = new_node # type: ignore
        self._size += 1

    def remove_beginning(self):
        if self.is_empty():
            raise IndexError("Pop from empty list")
        
        self.head = self.head.next # type: ignore
        self.head.previous = None  # type: ignore
        self._size -= 1

    def remove_by_index(self, index):
        self._valid_index(index)

        if index == 0:
            self.remove_beginning()
            return
        elif index == (self._size - 1):
            self.remove_end()
            return

        previous_node: TwoWaysNode = self.head # type: ignore
        for _ in range(index - 1):
            previous_node = previous_node.next # type: ignore

        pop_node: TwoWaysNode = previous_node.next # type: ignore
        previous_node.next = pop_node.next
        pop_node.next.previous = previous_node # type: ignore

        self._size -= 1

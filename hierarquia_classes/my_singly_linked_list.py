from base import LinearStruct, MethodNotImplemented
from typing import Iterator, Self, Any, Optional
from nodes import OneWayNode



class SinglyLinkedList(LinearStruct):

    def __init__(self) -> None:
        self.head: Optional[OneWayNode] = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def to_full(self) -> int:
        raise MethodNotImplemented()
    
    def is_full(self) -> bool:
        raise MethodNotImplemented()
    
    @classmethod
    def from_iter(cls, iter: Iterator) -> Self:
        ...

    def _valid_index(self, index: int):
        if index > self._size:
            raise IndexError(f"Linked list has {self._size} nodes, index {index} does not exist (starts on 0)")

    def insert_beginning(self, value: Any):
        self._size += 1
        new_node = OneWayNode(value)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, value: Any):
        self._size += 1
        new_node = OneWayNode(value)
        
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        for _ in range(self._size - 2):
            current_node: OneWayNode = current_node.next # type: ignore

        current_node.next = new_node

    def insert_by_index(self, value, index):
        self._valid_index(index)
        
        if index == 0:
            self.insert_beginning(value)
            return

        new_node = OneWayNode(value)

        previous_node: OneWayNode = self.head # type: ignore
        for _ in range(index - 1):
            previous_node = previous_node.next # type: ignore

        new_node.next = previous_node.next
        previous_node.next = new_node
        self._size += 1

    def set_value(self, value, index: int):
        self._valid_index(index)
        
        current_node: OneWayNode = self.head # type: ignore
        for _ in range(index):
            current_node = current_node.next # type: ignore

        current_node.value = value

    def remove_beginning(self):
        if self.is_empty():
            raise IndexError("Pop from empty list")
        
        self.head = self.head.next # type: ignore
        self._size -= 1

    def remove_end(self):
        if self.is_empty():
            raise IndexError("Pop from empty list")
        elif self._size == 1:
            self.remove_beginning()
            return
        
        current_node: OneWayNode = self.head # type: ignore
        for _ in range(self._size - 2):
            current_node = current_node.next # type: ignore

        del current_node.next
        current_node.next = None
        self._size -= 1
    
    def remove_by_index(self, index):
        self._valid_index(index)

        if index == 0:
            self.remove_beginning()
            return
        elif index == (self._size - 1):
            self.remove_end()
            return

        previous_node: OneWayNode = self.head # type: ignore
        for _ in range(index - 1):
            previous_node = previous_node.next # type: ignore

        pop_node: OneWayNode = previous_node.next # type: ignore
        previous_node.next = pop_node.next
        del pop_node

        self._size -= 1

    def get_beginning_item(self) -> Any:
        self._valid_index(0)
        return self.head.value # type: ignore
    
    def get_end_item(self) -> Any:
        self._valid_index(0)

        current_node = self.head # type: ignore
        for _ in range(self._size - 1):
            current_node: OneWayNode = current_node.next # type: ignore
        
        return current_node.value
    
    def get_index_item(self, index) -> Any:
        self._valid_index(index)
        if index == 0:
            return self.get_beginning_item()
        elif index == (self._size - 1):
            return self.get_end_item()

        current_node = self.head # type: ignore
        for _ in range(index):
            current_node: OneWayNode = current_node.next # type: ignore

        return current_node.value

    def __iter__(self):
        self.current_node = self.head
        return self

    def __next__(self):
        
        if self.current_node is not None:
            value = self.current_node.value
            self.current_node = self.current_node.next
            return value
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.get_index_item(index)

    def __setitem__(self, index, value):
        self.set_value(value, index)
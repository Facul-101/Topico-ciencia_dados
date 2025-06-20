from my_singly_linked_list import SinglyLinkedList
from typing import Type, Any


class Stack:

    def __init__(self, _type: Type, capacity: int) -> None:
        
        self._type = _type
        self._capacity = capacity
        self._data = SinglyLinkedList()

    def __len__(self) -> int:
        return self._data._size

    def is_empty(self) -> bool:
        return self._data.is_empty()
    
    def to_full(self) -> int:
        return self._capacity - self._data._size
    
    def is_full(self) -> bool:
        return self._data._size >= self._capacity

    def push(self, value: Any):
        
        if self.is_full():
            raise MemoryError("Stack overflow")
        elif type(value) is not self._type:
            raise ValueError(f"Expected {self._type} got {type(value)}")
        
        self._data.insert_end(value)
    
    def pop(self) -> Any:

        if self.is_empty():
            raise MemoryError("Stack underflow")

        value = self._data.get_end_item()
        self._data.remove_end()
        return value

    def swap(self):
        first_value = self.pop()
        second_value = self.pop()

        self.push(first_value)
        self.push(second_value)

from my_array import Array
from typing import Type, Any


class Queue:

    def __init__(self, _type: Type, capacity: int) -> None:
        
        self._type = _type
        self._capacity = capacity
        self._data = Array(_type, capacity)

    def __len__(self) -> int:
        return len(self._data)
    
    def is_empty(self) -> bool:
        return self._data.is_empty()
    
    def to_full(self) -> int:
        return self._data.to_full()
    
    def is_full(self) -> bool:
        return self._data.is_full()
    
    def insert(self, value):

        if self.is_full():
            raise MemoryError("Queue overflow")
        elif type(value) is not self._type:
            raise ValueError(f"Expected {self._type} got {type(value)}")
        
        self._data.insert_beginning(value)

    def pop(self) -> Any:

        if self.is_empty():
            raise MemoryError("Queue underflow")
        
        value = self._data.get_end_item()
        self._data.remove_end()
        return value
    
    def swap(self):
        first_value = self.pop()
        second_value = self.pop()

        self.insert(second_value)
        self.insert(first_value)

        for _ in range(len(self._data) - 2):
            self.insert(self.pop())
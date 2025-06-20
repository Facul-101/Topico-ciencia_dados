from base import LinearStruct, MethodNotImplemented
from typing import Iterator, Self, Type, Any
from copy import deepcopy


class Array(LinearStruct):

    def __init__(self, _type: Type, capacity: int = 6, dynamic: bool = False) -> None:
        assert capacity > 0, "Capacity must be greater then 0"
        
        self._type = _type
        self._capacity = capacity
        self._dynamic = dynamic
        self._data = []

    def __len__(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return len(self) == 0

    def to_full(self) -> int:
        return len(self) - self._capacity

    def is_full(self) -> bool:
        return self.to_full() == 0

    @classmethod
    def from_iter(cls, iter: Iterator) -> Self:
        ...

    def _grow_if_necessary(self):
        if self._dynamic and self.is_full():
            self._capacity *= 2
        elif self.is_full():
            raise ValueError("Can not add any more data, Array is full")

    def _fill_if_necessary(self, index: int):
        if self._capacity > index:
            return

        self._data += [None for _ in range(len(self._data), (index + 1))]

        while self._capacity < index:
            self._grow_if_necessary()

    def _valid_value(self, value: Any):
        if type(value) != self._type:
            raise ValueError(f"Type mismatch, expected {self._type} got {type(value)}")

    def _valid_index(self, index: int):
        if len(self._data) < index:
            raise IndexError(f"Value at index {index} not initialized")

    def insert_beginning(self, value: Any):
        self._valid_value(value)
        self._grow_if_necessary()
        return self._data.insert(0, value)

    def insert_end(self, value: Any):
        self._valid_value(value)
        self._grow_if_necessary()
        return self._data.append(value)

    def insert_by_index(self, value, index: int):
        self._valid_value(value)
        self._fill_if_necessary(index)
        return self._data.insert(index, value)

    def set_value(self, value: Any, index: int):
        self._valid_value(value)
        self._valid_index(index)
        return self._data.insert(index, value)

    def remove_beginning(self):
        self._data.pop(0)

    def remove_end(self):
        self._data.pop()

    def remove_by_index(self, index: int):
        self._valid_index(index)
        self._data.pop(index)

    def get_beginning_item(self):
        return deepcopy(self._data[0])

    def get_end_item(self):
        return deepcopy(self._data[-1])

    def get_index_item(self, index):
        self._valid_index(index)
        return deepcopy(self._data[index])

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        
        if self.current_index < len(self._data):
            value = self._data[self.current_index]
            self.current_index += 1
            return value
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.get_index_item(index)

    def __setitem__(self, index, value):
        self.set_value(value, index)

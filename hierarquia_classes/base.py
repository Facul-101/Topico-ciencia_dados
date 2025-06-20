from abc import ABC, abstractmethod
from typing import Self, Iterator, Any, Optional

class MethodNotImplemented(Exception):
    def __str__(self) -> str:
        return "This method is not implemented for this data structure"

class LinearStruct(ABC):

    # region 1
    @abstractmethod
    def __len__(self) -> int: pass
    # endregion
    
    # region 2
    @abstractmethod
    def is_empty(self) -> bool: pass
    
    @abstractmethod
    def to_full(self) -> int: pass # Returns the number os items to make the entity full
    
    @abstractmethod
    def is_full(self) -> bool: pass # Returns the number os items to make the entity full
    # endregion
    
    # region 3
    @classmethod
    @abstractmethod
    def from_iter(cls, iter: Iterator) -> Self: pass
    # endregion
    
    # region 4
    @abstractmethod
    def insert_beginning(self): pass

    @abstractmethod
    def insert_end(self): pass

    @abstractmethod
    def insert_by_index(self, value, index): pass
    # endregion
    
    # region 5
    @abstractmethod
    def set_value(self, value, index: Optional[Any]=None, possition: Optional[int]=None): pass
    # endregion
    
    # region 6
    @abstractmethod
    def remove_beginning(self): pass

    @abstractmethod
    def remove_end(self): pass

    @abstractmethod
    def remove_by_index(self, index): pass
    # endregion
    
    # region 7
    @abstractmethod
    def get_end_item(self) -> Any: pass

    @abstractmethod
    def get_beginning_item(self) -> Any: pass

    @abstractmethod
    def get_index_item(self, index) -> Any: pass

    @abstractmethod
    def __iter__(self): pass

    @abstractmethod
    def __next__(self): pass
    # endregion

    def __getitem__(self, index): pass

    def __setitem__(self, index, value): pass
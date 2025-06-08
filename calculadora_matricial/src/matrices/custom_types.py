from typing import Literal, TypeAlias, Union


ROOT_OPERATIONS: TypeAlias = Literal['+', '-']
STD_OPERATIONS: TypeAlias = Union[ROOT_OPERATIONS, Literal['*']]
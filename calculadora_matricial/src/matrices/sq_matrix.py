from .std_matrix import STDMatrix
from . import custom_types as ct
from typing import overload



class SQMatrix(STDMatrix):

    def __init__(self, data: list[list[float]]) -> None:
        self.check_valid(data)
        self.data = data
        self._shape = len(data)

    def get_transpose(self) -> "SQMatrix":
        return SQMatrix(self._transpose())

    def get_std_shape(self) -> tuple[int, int]:
            return (self._shape, self._shape)
            
    def check_valid(self, data: list[list[float]]):
        for line in data:
            if len(line) != len(data):
                raise ValueError("All lines must be the same length")

    def trace(self) -> float:
        return sum([line[i] for i, line in enumerate(self.data)])

    def _try_parse_sq(self, other: "SQMatrix|STDMatrix") -> "SQMatrix":

        if type(other) == SQMatrix:
            return other

        try:
            new_sq = SQMatrix(other.data)
        except Exception:
            raise ValueError(f"Parse error: {type(other)} -> {type(self)}")
        
        return new_sq

    @overload
    @classmethod
    def _mult(cls, left: "SQMatrix", right: "SQMatrix") -> "SQMatrix": ...
    @overload
    @classmethod
    def _mult(cls, left: "STDMatrix", right: "SQMatrix") -> "STDMatrix": ...
    @overload
    @classmethod
    def _mult(cls, left: "SQMatrix", right: "STDMatrix") -> "STDMatrix": ...
    @classmethod
    def _mult(cls, left: "SQMatrix|STDMatrix", right: "SQMatrix|STDMatrix") -> "SQMatrix|STDMatrix":
        assert type(left) == SQMatrix or type(right) == SQMatrix, "One of the matrices must be SQMatrix"
        
        if type(left) is STDMatrix:
            return super()._mult(left, STDMatrix(right.data))
        elif type(right) is STDMatrix:
            return super()._mult(STDMatrix(left.data), right)

        if left.get_std_shape() != right.get_std_shape():
            raise ValueError(f"Operação invalida, tamanho incompativel ({left.get_std_shape()} != {right.get_std_shape()})")
        
        assert type(left) == SQMatrix and type(right) == SQMatrix

        result_data: list[list[float]] = []
        for l in range(left.get_std_shape()[0]):
            line = []
            result_data.append(line)
            for c in range(right.get_std_shape()[0]):
                value = sum([left.data[l][i]*right.data[i][c] for i in range(left.get_std_shape()[0])])
                line.append(value)

        result_mtx = SQMatrix(result_data)
        return result_mtx
    
    def __add__(self, other: "SQMatrix|STDMatrix|int|float") -> "SQMatrix":
        assert isinstance(other, STDMatrix) or isinstance(other, int) or isinstance(other, float) \
        , "Other value must be a int or a float or be from STDMatrix class "

        if isinstance(other, int) or isinstance(other, float):
            return SQMatrix(self._num_operation(other, '+'))

        if self.get_std_shape() != other.get_std_shape():
            raise ValueError(f"Operação invalida, tamanho incompativel ({self.get_std_shape()} != {other.get_std_shape()})")

        return SQMatrix(self._mtx_operation(other, '+'))
    
    def __radd__(self, other: "SQMatrix|STDMatrix|int|float") -> "SQMatrix":
        return self.__add__(other)
    
    def __sub__(self, other: "SQMatrix|STDMatrix|int|float") -> "SQMatrix":
        assert isinstance(other, STDMatrix) or isinstance(other, int) or isinstance(other, float) \
        , "Other value must be a int or a float or be from STDMatrix class "

        if isinstance(other, int) or isinstance(other, float):
            return SQMatrix(self._num_operation(other, '-'))
        
        sq_other = self._try_parse_sq(other)

        if self.get_std_shape() != sq_other.get_std_shape():
            raise ValueError(f"Operação invalida, tamanho incompativel ({self.get_std_shape()} != {sq_other.get_std_shape()})")

        return SQMatrix(self._mtx_operation(sq_other, '-'))
    
    def __rsub__(self, other: "SQMatrix|STDMatrix|int|float") -> "SQMatrix":
        return (-self).__add__(other)
    
    def __mul__(self, other: "SQMatrix|STDMatrix|int|float") -> "SQMatrix|STDMatrix":
        assert isinstance(other, STDMatrix) or isinstance(other, int) or isinstance(other, float) \
        , "Other value must be a int or a float or be from STDMatrix class "

        if isinstance(other, int) or isinstance(other, float):
            return SQMatrix(self._num_operation(other, '*'))
        
        return SQMatrix._mult(self, other)
    
    def __rmul__(self, other: "SQMatrix|STDMatrix|int|float") -> "SQMatrix|STDMatrix":
        assert isinstance(other, STDMatrix) or isinstance(other, int) or isinstance(other, float) \
        , "Other value must be a int or a float or be from STDMatrix class "

        if isinstance(other, int) or isinstance(other, float):
            return SQMatrix(self._num_operation(other, '*'))
        
        return SQMatrix._mult(other, self)

    def __neg__(self) -> "SQMatrix":
        return SQMatrix(self._num_operation(-1, '*'))

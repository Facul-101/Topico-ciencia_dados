from .sq_matrix import SQMatrix
from .std_matrix import STDMatrix
from .trg_matrix import TRGMatrix
from typing import overload
from copy import deepcopy



class UPTMatrix(TRGMatrix):
    
    def get_determinant(self) -> float:

        det = 1
        for l in self.data:
            det *= l[0]

        return det
    
    def check_valid(self, data: list[list[float]]):
        for i, line in enumerate(data[::-1], start=1):
            if len(line) != i:
                raise ValueError("Dados inválidos - UPTMatrix")

    def fill_lines(self) -> list[list[float]]:
        new_data: list[list[float]] = []
        for line in self.data:
            new_line = deepcopy(line)
            new_data.append(new_line)
            for _ in range(self.get_std_shape()[0] - len(line)):
                new_line.insert(0, 0.0)
        
        return new_data

    def trace(self) -> float:
        return sum([line[0] for line in self.data])

    @overload
    @classmethod
    def _mult(cls, left: "UPTMatrix", right: "UPTMatrix") -> "UPTMatrix": ...
    @overload
    @classmethod
    def _mult(cls, left: "UPTMatrix", right: "SQMatrix") -> "SQMatrix": ...
    @overload
    @classmethod
    def _mult(cls, left: "SQMatrix", right: "UPTMatrix") -> "SQMatrix": ...
    @overload
    @classmethod
    def _mult(cls, left: "UPTMatrix", right: "STDMatrix") -> "STDMatrix": ...
    @overload
    @classmethod
    def _mult(cls, left: "STDMatrix", right: "UPTMatrix") -> "STDMatrix": ...
    @classmethod
    def _mult(cls, left: "UPTMatrix|SQMatrix|STDMatrix", right: "UPTMatrix|SQMatrix|STDMatrix") -> "UPTMatrix|SQMatrix|STDMatrix":
        assert type(left) == UPTMatrix or type(right) == UPTMatrix, "One of the matrices must be UPTMatrix"
        
        result = super()._mult(left, right)

        if result is not None:
            return result
        
        assert type(left) == UPTMatrix and type(right) == UPTMatrix
        
        r_shape = right.get_std_shape()
        l_shape = left.get_std_shape()

        if l_shape != r_shape:
            raise ValueError(f"Operação invalida, tamanho incompativel ({l_shape} != {r_shape})")

        result_data: list[list[float]] = []
        for n_lin in range(l_shape[0]):
            line = []
            result_data.append(line)
            for n_col in range(n_lin, l_shape[0]):
                
                value = 0                
                for i in range(l_shape[0]):
                    left_col = i - n_lin
                    right_col = n_col - i
                    if left_col >= 0 and right_col >= 0:
                        value += left.data[n_lin][left_col]*right.data[i][right_col]

                line.append(value)

        result_mtx = UPTMatrix(result_data)
        return result_mtx

    def __add__(self, other: "UPTMatrix|SQMatrix|STDMatrix|int|float") -> "UPTMatrix|SQMatrix":
        assert isinstance(other, STDMatrix) or isinstance(other, int) or isinstance(other, float) \
        , "Other value must be a int or a float or be from STDMatrix class "

        if isinstance(other, int) or isinstance(other, float):
            return UPTMatrix(self._num_operation(other, '+'))

        if self.get_std_shape() != other.get_std_shape():
            raise ValueError(f"Operação invalida, tamanho incompativel ({self.get_std_shape()} != {other.get_std_shape()})")
        
        new_data = self._mtx_operation(other, '+')

        if type(other) == UPTMatrix:
            return UPTMatrix(new_data)
        else:
            return SQMatrix(new_data)
    
    def __radd__(self, other: "UPTMatrix|SQMatrix|STDMatrix|int|float") -> "UPTMatrix|SQMatrix":
        return self.__add__(other)
    
    def __sub__(self, other: "UPTMatrix|SQMatrix|STDMatrix|int|float") -> "UPTMatrix|SQMatrix":
        assert isinstance(other, STDMatrix) or isinstance(other, int) or isinstance(other, float) \
        , "Other value must be a int or a float or be from STDMatrix class "

        if isinstance(other, int) or isinstance(other, float):
            return UPTMatrix(self._num_operation(other, '-'))

        if self.get_std_shape() != other.get_std_shape():
            raise ValueError(f"Operação invalida, tamanho incompativel ({self.get_std_shape()} != {other.get_std_shape()})")
        
        new_data = self._mtx_operation(other, '-')

        if type(other) == UPTMatrix:
            return UPTMatrix(new_data)
        else:
            return SQMatrix(new_data)
    
    def __rsub__(self, other: "UPTMatrix|SQMatrix|STDMatrix|int|float") -> "UPTMatrix|SQMatrix":
        return (-self).__add__(other)
    
    def __mul__(self, other: "UPTMatrix|SQMatrix|STDMatrix|int|float") -> "UPTMatrix|SQMatrix|STDMatrix":
        assert isinstance(other, STDMatrix) or isinstance(other, int) or isinstance(other, float) \
        , "Other value must be a int or a float or be from STDMatrix class "

        if isinstance(other, int) or isinstance(other, float):
            return UPTMatrix(self._num_operation(other, '*'))
        
        return UPTMatrix._mult(self, other)
    
    def __rmul__(self, other: "UPTMatrix|SQMatrix|STDMatrix|int|float") -> "UPTMatrix|SQMatrix|STDMatrix":
        assert isinstance(other, STDMatrix) or isinstance(other, int) or isinstance(other, float) \
        , "Other value must be a int or a float or be from STDMatrix class "

        if isinstance(other, int) or isinstance(other, float):
            return UPTMatrix(self._num_operation(other, '*'))
        
        return UPTMatrix._mult(other, self)

    def __neg__(self) -> "UPTMatrix":
        return UPTMatrix(self._num_operation(-1, '*'))

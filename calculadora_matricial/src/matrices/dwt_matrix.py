from .sq_matrix import SQMatrix
from .std_matrix import STDMatrix
from .trg_matrix import TRGMatrix
from .upt_matrix import UPTMatrix
from typing import overload
from copy import deepcopy



class DWTMatrix(TRGMatrix):

    def get_determinant(self) -> float:

        det = 1
        for l in self.data:
            det *= l[-1]

        return det

    def check_valid(self, data: list[list[float]]):
        for i, line in enumerate(data[::-1]):
            if len(line) != len(data) - i:
                raise ValueError("Dados inválidos - DIGMatrix")

    def fill_lines(self) -> list[list[float]]:
        new_data: list[list[float]] = []
        for line in self.data:
            new_line = deepcopy(line)
            new_data.append(new_line)
            for _ in range(self.get_std_shape()[0] - len(line)):
                new_line.append(0.0)
        
        return new_data

    @overload
    @classmethod
    def _mult(cls, left: "DWTMatrix", right: "DWTMatrix") -> "DWTMatrix": ...
    @overload
    @classmethod
    def _mult(cls, left: "DWTMatrix", right: "SQMatrix") -> "SQMatrix": ...
    @overload
    @classmethod
    def _mult(cls, left: "SQMatrix", right: "DWTMatrix") -> "SQMatrix": ...
    @overload
    @classmethod
    def _mult(cls, left: "DWTMatrix", right: "UPTMatrix") -> "SQMatrix": ...
    @overload
    @classmethod
    def _mult(cls, left: "UPTMatrix", right: "DWTMatrix") -> "SQMatrix": ...
    @overload
    @classmethod
    def _mult(cls, left: "DWTMatrix", right: "STDMatrix") -> "STDMatrix": ...
    @overload
    @classmethod
    def _mult(cls, left: "STDMatrix", right: "DWTMatrix") -> "STDMatrix": ...
    @classmethod
    def _mult(cls, left: "DWTMatrix|UPTMatrix|SQMatrix|STDMatrix", right: "DWTMatrix|UPTMatrix|SQMatrix|STDMatrix") -> "DWTMatrix|SQMatrix|STDMatrix":
        assert type(left) == DWTMatrix or type(right) == DWTMatrix, "One of the matrices must be DWTMatrix"
        
        result = super()._mult(left, right)

        if result is not None:
            return result

        if type(left) == UPTMatrix:
            assert isinstance(right, DWTMatrix)
            return SQMatrix._mult(SQMatrix(left.fill_lines()), SQMatrix(right.fill_lines()))
        
        elif type(right) == UPTMatrix:
            assert isinstance(left, DWTMatrix)
            return SQMatrix._mult(SQMatrix(left.fill_lines()), SQMatrix(right.fill_lines()))
        
        assert type(left) == DWTMatrix and type(right) == DWTMatrix
        
        r_shape = right.get_std_shape()
        l_shape = left.get_std_shape()

        if l_shape != r_shape:
            raise ValueError(f"Operação invalida, tamanho incompativel ({l_shape} != {r_shape})")

        result_data: list[list[float]] = []
        for n_lin in range(l_shape[0]):
            line = []
            result_data.append(line)
            for n_col in range(n_lin + 1):
                
                value = 0
                for i in range(l_shape[0]):
                    if i >= n_col and n_lin >= i:
                        value += left.data[n_lin][i]*right.data[i][n_col]

                line.append(value)

        result_mtx = DWTMatrix(result_data)
        return result_mtx

    def __add__(self, other: "DWTMatrix|UPTMatrix|SQMatrix|STDMatrix|int|float") -> "DWTMatrix|SQMatrix":
        assert isinstance(other, STDMatrix) or isinstance(other, int) or isinstance(other, float) \
        , "Other value must be a int or a float or be from STDMatrix class "

        if isinstance(other, int) or isinstance(other, float):
            return DWTMatrix(self._num_operation(other, '+'))

        if self.get_std_shape() != other.get_std_shape():
            raise ValueError(f"Operação invalida, tamanho incompativel ({self.get_std_shape()} != {other.get_std_shape()})")
        
        new_data = self._mtx_operation(other, '+')

        if type(other) == DWTMatrix:
            return DWTMatrix(new_data)
        else:
            return SQMatrix(new_data)
    
    def __radd__(self, other: "DWTMatrix|SQMatrix|STDMatrix|int|float") -> "DWTMatrix|SQMatrix":
        return self.__add__(other)
    
    def __sub__(self, other: "DWTMatrix|SQMatrix|STDMatrix|int|float") -> "DWTMatrix|SQMatrix":
        assert isinstance(other, STDMatrix) or isinstance(other, int) or isinstance(other, float) \
        , "Other value must be a int or a float or be from STDMatrix class "

        if isinstance(other, int) or isinstance(other, float):
            return DWTMatrix(self._num_operation(other, '-'))

        if self.get_std_shape() != other.get_std_shape():
            raise ValueError(f"Operação invalida, tamanho incompativel ({self.get_std_shape()} != {other.get_std_shape()})")
        
        new_data = self._mtx_operation(other, '-')

        if type(other) == DWTMatrix:
            return DWTMatrix(new_data)
        else:
            return SQMatrix(new_data)
    
    def __rsub__(self, other: "DWTMatrix|SQMatrix|STDMatrix|int|float") -> "DWTMatrix|SQMatrix":
        return (-self).__add__(other)
    
    def __mul__(self, other: "DWTMatrix|SQMatrix|STDMatrix|int|float") -> "DWTMatrix|SQMatrix|STDMatrix":
        assert isinstance(other, STDMatrix) or isinstance(other, int) or isinstance(other, float) \
        , "Other value must be a int or a float or be from STDMatrix class "

        if isinstance(other, int) or isinstance(other, float):
            return DWTMatrix(self._num_operation(other, '*'))
        
        return DWTMatrix._mult(self, other)
    
    def __rmul__(self, other: "DWTMatrix|SQMatrix|STDMatrix|int|float") -> "DWTMatrix|SQMatrix|STDMatrix":
        assert isinstance(other, STDMatrix) or isinstance(other, int) or isinstance(other, float) \
        , "Other value must be a int or a float or be from STDMatrix class "

        if isinstance(other, int) or isinstance(other, float):
            return DWTMatrix(self._num_operation(other, '*'))
        
        return DWTMatrix._mult(other, self)

    def __neg__(self) -> "DWTMatrix":
        return DWTMatrix(self._num_operation(-1, '*'))

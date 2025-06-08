from .sq_matrix import SQMatrix
from .std_matrix import STDMatrix
from .trg_matrix import TRGMatrix
from .upt_matrix import UPTMatrix
from .dwt_matrix import DWTMatrix
from . import custom_types as ct
from typing import overload
from copy import deepcopy



class DIGMatrix(TRGMatrix):

    def __init__(self, data: list[float]) -> None:
        self.check_valid(data)
        self.data: list[float] = data
        self._shape = len(data)

    def check_valid(self, data: list[float]):

        for i in data:
            if not isinstance(i, float) and not isinstance(i, int):
                raise ValueError("Dados inválidos - DIGMatrix")

    def get_transpose(self) -> "DIGMatrix":
        return self

    def get_determinant(self) -> float:

        det = 1
        for l in self.data:
            det *= l

        return det

    def fill_lines(self) -> list[list[float]]:
        
        new_data: list[list[float]] = []
        for i, value in enumerate(self.data):
            line = [0.0]*i + [value] + [0.0]*(self._shape - (i + 1))
            new_data.append(line)
        
        return new_data

    def fill_lines_up(self):
        new_data: list[list[float]] = []
        for i, value in enumerate(self.data, start=1):
            line = [value] + [0.0]*(self._shape - i)
            new_data.append(line)
        
        return new_data
    
    def fill_lines_down(self):
        new_data: list[list[float]] = []
        for i, value in enumerate(self.data):
            line = [0.0]*i + [value]
            new_data.append(line)
        
        return new_data

    def _num_operation(self, other: int|float, type: ct.STD_OPERATIONS) -> list[float]:
        
        operations: dict[ct.STD_OPERATIONS, str] = {
            '+': "value + other",
            '*': "value * other",
            '-': "value - other"
        }

        result_data = [eval(operations[type]) for value in self.data]

        return result_data

    def _mtx_operation(self, other: "DIGMatrix", type_: ct.ROOT_OPERATIONS) -> list[float]:
        
        result_data: list[float]

        if type_ == '+':
            result_data = deepcopy(other.data)
        elif type_ == '-':
            result_data = deepcopy((-other).data)

        for i, value in enumerate(self.data):
            result_data[i] += value

        return result_data

    @overload
    @classmethod
    def _mult(cls, left: "DIGMatrix", right: "DIGMatrix") -> "DIGMatrix": ...
    @overload
    @classmethod
    def _mult(cls, left: "DIGMatrix", right: "UPTMatrix") -> "UPTMatrix": ...
    @overload
    @classmethod
    def _mult(cls, left: "UPTMatrix", right: "DIGMatrix") -> "UPTMatrix": ...
    @overload
    @classmethod
    def _mult(cls, left: "DIGMatrix", right: "DWTMatrix") -> "DWTMatrix": ...
    @overload
    @classmethod
    def _mult(cls, left: "DWTMatrix", right: "DIGMatrix") -> "DWTMatrix": ...
    @overload
    @classmethod
    def _mult(cls, left: "DIGMatrix", right: "SQMatrix") -> "SQMatrix": ...
    @overload
    @classmethod
    def _mult(cls, left: "SQMatrix", right: "DIGMatrix") -> "SQMatrix": ...
    @overload
    @classmethod
    def _mult(cls, left: "DIGMatrix", right: "STDMatrix") -> "STDMatrix": ...
    @overload
    @classmethod
    def _mult(cls, left: "STDMatrix", right: "DIGMatrix") -> "STDMatrix": ...
    @classmethod
    def _mult(cls, left: "DIGMatrix|DWTMatrix|UPTMatrix|SQMatrix|STDMatrix", right: "DIGMatrix|DWTMatrix|UPTMatrix|SQMatrix|STDMatrix") -> "DIGMatrix|DWTMatrix|SQMatrix|STDMatrix":
        assert type(left) == DIGMatrix or type(right) == DIGMatrix, "One of the matrices must be DWTMatrix"

        result = super()._mult(left, right)

        if result is not None:
            return result
        
        if type(left) == UPTMatrix:
            assert isinstance(right, DIGMatrix)
            return UPTMatrix._mult(left, UPTMatrix(right.fill_lines_up()))
        
        elif type(right) == UPTMatrix:
            assert isinstance(left, DIGMatrix)
            return UPTMatrix._mult(UPTMatrix(left.fill_lines_up()), right)
        
        elif type(left) == DWTMatrix:
            assert isinstance(right, DIGMatrix)
            return DWTMatrix._mult(left, DWTMatrix(right.fill_lines_down()))
        
        elif type(right) == DWTMatrix:
            assert isinstance(left, DIGMatrix)
            return DWTMatrix._mult(DWTMatrix(left.fill_lines_down()), right)
        
        assert isinstance(left, DIGMatrix) and isinstance(right, DIGMatrix)

        r_shape = right.get_std_shape()
        l_shape = left.get_std_shape()

        if l_shape != r_shape:
            raise ValueError(f"Operação invalida, tamanho incompativel ({l_shape} != {r_shape})")

        result_data: list[float] = []
        for v_l, v_r in zip(left.data, right.data):
            result_data.append(v_l*v_r)

        result_mtx = DIGMatrix(result_data)
        return result_mtx
    
    def __add__(self, other: "DIGMatrix|DWTMatrix|UPTMatrix|SQMatrix|STDMatrix|int|float") -> "DIGMatrix|DWTMatrix|UPTMatrix|SQMatrix":
        assert isinstance(other, STDMatrix) or isinstance(other, int) or isinstance(other, float) \
        , "Other value must be a int or a float or be from STDMatrix class "

        if isinstance(other, int) or isinstance(other, float):
            return DIGMatrix(self._num_operation(other, '+'))
        
        if self.get_std_shape() != other.get_std_shape():
            raise ValueError(f"Operação invalida, tamanho incompativel ({self.get_std_shape()} != {other.get_std_shape()})")
        
        if type(other) == UPTMatrix:
            return other.__add__(UPTMatrix(self.fill_lines_up()))
        
        elif type(other) == DWTMatrix:
            return other.__add__(DWTMatrix(self.fill_lines_down()))
        
        elif type(other) == SQMatrix:
            return other.__add__(SQMatrix(self.fill_lines()))
        
        elif type(other) == STDMatrix:
            return SQMatrix(self.fill_lines()).__add__(other)
        
        assert type(other) == DIGMatrix
        return DIGMatrix(self._mtx_operation(other, '+'))
    
    def __radd__(self, other: "DIGMatrix|DWTMatrix|UPTMatrix|SQMatrix|STDMatrix|int|float") -> "DIGMatrix|DWTMatrix|UPTMatrix|SQMatrix":
        return self.__add__(other)

    def __sub__(self, other: SQMatrix | STDMatrix | int | float) -> SQMatrix:
        assert isinstance(other, STDMatrix) or isinstance(other, int) or isinstance(other, float) \
        , "Other value must be a int or a float or be from STDMatrix class "

        if isinstance(other, int) or isinstance(other, float):
            return DIGMatrix(self._num_operation(other, '-'))
        
        if self.get_std_shape() != other.get_std_shape():
            raise ValueError(f"Operação invalida, tamanho incompativel ({self.get_std_shape()} != {other.get_std_shape()})")
        
        if type(other) == UPTMatrix:
            return UPTMatrix(self.fill_lines_up()).__sub__(other)
        
        elif type(other) == DWTMatrix:
            return DWTMatrix(self.fill_lines_down()).__sub__(other)
        
        elif type(other) == SQMatrix:
            return SQMatrix(self.fill_lines()).__sub__(other)
        
        elif type(other) == STDMatrix:
            return SQMatrix(self.fill_lines()).__sub__(other)
        
        assert type(other) == DIGMatrix
        return DIGMatrix(self._mtx_operation(other, '-'))

    def __rsub__(self, other: "DIGMatrix|DWTMatrix|UPTMatrix|SQMatrix|STDMatrix|int|float") -> "DIGMatrix|DWTMatrix|UPTMatrix|SQMatrix":
        return (-self).__add__(other)

    def __mul__(self, other: "DIGMatrix|DWTMatrix|UPTMatrix|SQMatrix|STDMatrix|int|float") -> "DIGMatrix|DWTMatrix|UPTMatrix|SQMatrix|STDMatrix":
        assert isinstance(other, STDMatrix) or isinstance(other, int) or isinstance(other, float) \
        , "Other value must be a int or a float or be from STDMatrix class "

        if isinstance(other, int) or isinstance(other, float):
            return DIGMatrix(self._num_operation(other, '*'))
        
        return DIGMatrix._mult(self, other)
    
    def __rmul__(self, other: "DIGMatrix|DWTMatrix|UPTMatrix|SQMatrix|STDMatrix|int|float") -> "DIGMatrix|DWTMatrix|UPTMatrix|SQMatrix|STDMatrix":
        assert isinstance(other, STDMatrix) or isinstance(other, int) or isinstance(other, float) \
        , "Other value must be a int or a float or be from STDMatrix class "

        if isinstance(other, int) or isinstance(other, float):
            return DIGMatrix(self._num_operation(other, '*'))
        
        return DIGMatrix._mult(other, self)

    def __neg__(self) -> "DIGMatrix":
        return DIGMatrix(self._num_operation(-1, '*'))
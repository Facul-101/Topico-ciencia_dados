from .sq_matrix import SQMatrix
from .std_matrix import STDMatrix
from . import custom_types as ct
from copy import deepcopy


class TRGMatrix(SQMatrix):
    
    def get_determinant(self) -> float:
        raise Exception("Method check_valid not implemented for TRGMatrix")

    def check_valid(self, data: list[list[float]]):
        raise Exception("Method check_valid not implemented for TRGMatrix")
    
    def fill_lines(self) -> list[list[float]]:
        raise Exception("Method fill_lines not implemented for TRGMatrix")

    def get_transpose(self) -> SQMatrix:
        return SQMatrix(SQMatrix(self.fill_lines())._transpose())

    @classmethod
    def _mult(cls, left: "TRGMatrix|SQMatrix|STDMatrix", right: "TRGMatrix|SQMatrix|STDMatrix") -> "None|SQMatrix|STDMatrix":
        
        if type(left) == SQMatrix:
            assert isinstance(right, TRGMatrix)
            return SQMatrix._mult(left, SQMatrix(right.fill_lines()))
        
        elif type(right) == SQMatrix:
            assert isinstance(left, TRGMatrix)
            return SQMatrix._mult(SQMatrix(left.fill_lines()), right)
        
        elif type(left) == STDMatrix:
            assert isinstance(right, TRGMatrix)
            return STDMatrix._mult(left, STDMatrix(right.fill_lines()))
        
        elif type(right) == STDMatrix:
            assert isinstance(left, TRGMatrix)
            return STDMatrix._mult(STDMatrix(left.fill_lines()), right)
    
        return None
    
    def _mtx_operation(self, other: "STDMatrix", type_: ct.ROOT_OPERATIONS) -> list[list[float]]:
        if not isinstance(other, TRGMatrix):
            super()._mtx_operation(other, type_)

        result_data: list[list[float]]
        if type_ == '+':
            result_data = deepcopy(other.data)
        elif type_ == '-':
            result_data = deepcopy((-other).data)

        for i, line in enumerate(self.data):
            for j, value in enumerate(line):
                result_data[i][j] += value

        return result_data

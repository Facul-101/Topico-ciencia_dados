from . import custom_types as ct


class STDMatrix:

    def __init__(self, data: list[list[float]]) -> None:
        self.check_valid(data)

        self.data: list[list[float]] = data
        self._shape = (len(self.data), len(self.data[0])) # Linnha, coluna
    
    def show(self):
        print("Dado cru: ", self.data)

        print("Matriz resultado:")
        data = self.data
        try:
            data = self.fill_lines() # type: ignore
        except Exception:
            pass

        for row in data:
            print(" ".join(f"{val:8.2f}" for val in row))

    def get_std_shape(self) -> tuple[int, int]:
        return self._shape

    def check_valid(self, data):
        for line in data[1:]:
            if len(line) != len(data[0]):
                raise ValueError("All lines must be the same length")

    def _transpose(self) -> list[list[float]]:
        return [[linha[i] for linha in self.data] for i in range(len(self.data[0]))]

    def get_transpose(self) -> "STDMatrix":
        return STDMatrix(self._transpose())

    def _num_operation(self, other: int|float, type: ct.STD_OPERATIONS) -> list[list[float]]:

        operations: dict[ct.STD_OPERATIONS, str] = {
            '+': "value + other",
            '*': "value * other",
            '-': "value - other"
        }

        result_data = [[eval(operations[type]) for value in line] for line in self.data]

        return result_data

    def _mtx_operation(self, other: "STDMatrix", type_: ct.ROOT_OPERATIONS) -> list[list[float]]:
        
        operations: dict[ct.STD_OPERATIONS, str] = {
            '+': "v_a + v_b",
            '-': "v_a - v_b"
        }

        result_data = [[eval(operations[type_]) for v_a, v_b in zip(l_a, l_b)] for l_a, l_b in zip(self.data, other.data)]
        return result_data
    
    @classmethod
    def _mult(cls, left: "STDMatrix", right: "STDMatrix") -> "STDMatrix":
        
        if left.get_std_shape()[1] != right.get_std_shape()[0]:
            raise ValueError(f"Operação invalida, tamanho incompativel ({left.get_std_shape()} != {right.get_std_shape()})")

        result_data: list[list[float]] = []
        for l in range(left.get_std_shape()[0]):
            line = []
            result_data.append(line)
            for c in range(right.get_std_shape()[1]):
                value = sum([left.data[l][i]*right.data[i][c] for i in range(left.get_std_shape()[1])])
                line.append(value)

        result_mtx = STDMatrix(result_data)
        return result_mtx

    def __add__(self, other: "STDMatrix|int|float") -> "STDMatrix":
        assert isinstance(other, STDMatrix) or isinstance(other, int) or isinstance(other, float) \
        , "Other value must be a int or a float or be from STDMatrix class "

        if isinstance(other, int) or isinstance(other, float):
            return STDMatrix(self._num_operation(other, '+'))

        if self.get_std_shape() != other.get_std_shape():
            raise ValueError(f"Operação invalida, tamanho incompativel ({self.get_std_shape()} != {other.get_std_shape()})")

        return STDMatrix(self._mtx_operation(other, '+'))
    
    def __radd__(self, other: "STDMatrix|int|float") -> "STDMatrix":
        return self.__add__(other)
    
    def __sub__(self, other: "STDMatrix|int|float") -> "STDMatrix":
        assert isinstance(other, STDMatrix) or isinstance(other, int) or isinstance(other, float) \
        , "Other value must be a int or a float or be from STDMatrix class "

        if isinstance(other, int) or isinstance(other, float):
            return STDMatrix(self._num_operation(other, '-'))

        if self.get_std_shape() != other.get_std_shape():
            raise ValueError(f"Operação invalida, tamanho incompativel ({self.get_std_shape()} != {other.get_std_shape()})")

        return STDMatrix(self._mtx_operation(other, '-'))
    
    def __rsub__(self, other: "STDMatrix|int|float") -> "STDMatrix":
        return (-self).__add__(other)
    
    def __mul__(self, other: "STDMatrix|int|float") -> "STDMatrix":
        assert isinstance(other, STDMatrix) or isinstance(other, int) or isinstance(other, float) \
        , "Other value must be a int or a float or be from STDMatrix class "

        if isinstance(other, int) or isinstance(other, float):
            return STDMatrix(self._num_operation(other, '*'))
        
        return STDMatrix._mult(self, other)
    
    def __rmul__(self, other: "STDMatrix|int|float") -> "STDMatrix":
        assert isinstance(other, STDMatrix) or isinstance(other, int) or isinstance(other, float) \
        , "Other value must be a int or a float or be from STDMatrix class "

        if isinstance(other, int) or isinstance(other, float):
            return STDMatrix(self._num_operation(other, '*'))
        
        return STDMatrix._mult(other, self)

    def __neg__(self) -> "STDMatrix":
        return STDMatrix(self._num_operation(-1, '*'))

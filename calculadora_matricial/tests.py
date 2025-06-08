import pytest
from src.matrices.std_matrix import STDMatrix
from src.matrices.sq_matrix import SQMatrix
from src.matrices.trg_matrix import TRGMatrix
from src.matrices.upt_matrix import UPTMatrix
from src.matrices.dwt_matrix import DWTMatrix
from src.matrices.dig_matrix import DIGMatrix

# Run tests:
# pytest calculadora_matricial/tests.py

# region STDMatrix tests

def test_std_init_valid():
    m = STDMatrix([[1, 2], [3, 4]])
    assert m.get_std_shape() == (2, 2)
    assert m.data == [[1, 2], [3, 4]]

def test_std_init_invalid():
    with pytest.raises(ValueError):
        STDMatrix([[1, 2], [3]])

def test_std_neg():
    m = -STDMatrix([[1, 2], [3, 4]])
    assert m.get_std_shape() == (2, 2)
    assert m.data == [[-1, -2], [-3, -4]]

def test_std_t():
    a = STDMatrix([[1, 2], [1, 2]])
    b = a.get_transpose()
    assert b.data == [[1, 1], [2, 2]]

def test_std_add_matrix():
    a = STDMatrix([[1, 2], [3, 4]])
    b = STDMatrix([[5, 6], [7, 8]])
    c = a + b
    assert c.data == [[6, 8], [10, 12]]

def test_std_add_scalar():
    a = STDMatrix([[1, 2], [3, 4]])
    
    b = 10 + a
    assert b.data == [[11, 12], [13, 14]]
    
    c = a + 10
    assert c.data == [[11, 12], [13, 14]]

def test_std_sub_nmatrix():
    a = STDMatrix([[5, 7], [9, 11]])
    b = STDMatrix([[1, 2], [3, 4]])
    c = a - b
    assert c.data == [[4, 5], [6, 7]]

def test_std_sub_scalar():
    a = STDMatrix([[1, 2], [3, 4]])
    
    b = 10 - a
    assert b.data == [[9, 8], [7, 6]]
    
    c = a - 10
    assert c.data == [[-9, -8], [-7, -6]]

def test_std_mul_matrix():
    a = STDMatrix([[1, 2], [3, 4]])
    b = STDMatrix([[2, 0], [1, 2]])
    c = a * b
    assert c.data == [[4, 4], [10, 8]]

def test_std_mul_scalar():
    a = STDMatrix([[1, 2], [3, 4]])
    
    b = 2 * a
    assert b.data == [[2, 4], [6, 8]]
    
    c = a * 2
    assert c.data == [[2, 4], [6, 8]]

def test_std_add_shape_error():
    a = STDMatrix([[1, 2]])
    b = STDMatrix([[1, 2], [3, 4]])
    with pytest.raises(ValueError):
        _ = a + b

def test_std_sub_shape_error():
    a = STDMatrix([[1, 2]])
    b = STDMatrix([[1, 2], [3, 4]])
    with pytest.raises(ValueError):
        _ = a - b

def test_std_mul_shape_error():
    a = STDMatrix([[1, 2, 3], [4, 5, 6]])
    b = STDMatrix([[1, 2], [3, 4]])
    with pytest.raises(ValueError):
        _ = a * b

# endregion

# region SQMatrix tests

def test_sq_init_valid():
    m = SQMatrix([[1, 2], [3, 4]])
    assert m.get_std_shape() == (2, 2)
    assert m.data == [[1, 2], [3, 4]]

def test_sq_init_invalid():
    with pytest.raises(ValueError):
        SQMatrix([[1, 2], [3]])

def test_sq_neg():
    m = -SQMatrix([[1, 2], [3, 4]])
    assert m.get_std_shape() == (2, 2)
    assert m.data == [[-1, -2], [-3, -4]]

def test_sq_t():
    a = SQMatrix([[1, 2], [1, 2]])
    b = a.get_transpose()
    assert b.data == [[1, 1], [2, 2]]

def test_sq_add_matrix():
    a = SQMatrix([[1, 2], [3, 4]])
    b = SQMatrix([[5, 6], [7, 8]])
    c = a + b
    assert c.data == [[6, 8], [10, 12]]

    a = SQMatrix([[1, 2], [3, 4]])
    b = STDMatrix([[5, 6], [7, 8]])
    c = a + b
    assert type(c) is SQMatrix
    assert c.data == [[6, 8], [10, 12]]

    a = STDMatrix([[1, 2], [3, 4]])
    b = SQMatrix([[5, 6], [7, 8]])
    c = a + b
    assert type(c) is SQMatrix
    assert c.data == [[6, 8], [10, 12]]

def test_sq_add_scalar():
    a = SQMatrix([[1, 2], [3, 4]])
    
    b = 10 + a
    assert b.data == [[11, 12], [13, 14]]
    
    c = a + 10
    assert c.data == [[11, 12], [13, 14]]

def test_sq_sub_nmatrix():
    a = SQMatrix([[5, 7], [9, 11]])
    b = SQMatrix([[1, 2], [3, 4]])
    c = a - b
    assert c.data == [[4, 5], [6, 7]]

    a = SQMatrix([[5, 7], [9, 11]])
    b = STDMatrix([[1, 2], [3, 4]])
    c = a - b
    assert type(c) is SQMatrix
    assert c.data == [[4, 5], [6, 7]]

    a = STDMatrix([[5, 7], [9, 11]])
    b = SQMatrix([[1, 2], [3, 4]])
    c = a - b
    assert type(c) is SQMatrix
    assert c.data == [[4, 5], [6, 7]]

def test_sq_sub_scalar():
    a = SQMatrix([[1, 2], [3, 4]])
    
    b = 10 - a
    assert b.data == [[9, 8], [7, 6]]
    
    c = a - 10
    assert c.data == [[-9, -8], [-7, -6]]

def test_sq_mul_matrix():
    a = SQMatrix([[1, 2], [3, 4]])
    b = SQMatrix([[2, 0], [1, 2]])
    c = a * b
    assert c.data == [[4, 4], [10, 8]]

    a = SQMatrix([[1, 2], [3, 4]])
    b = STDMatrix([[2, 0], [1, 2]])
    c = a * b
    assert type(c) is STDMatrix
    assert c.data == [[4, 4], [10, 8]]

    a = STDMatrix([[1, 2], [3, 4]])
    b = SQMatrix([[2, 0], [1, 2]])
    c = a * b
    assert type(c) is STDMatrix
    assert c.data == [[4, 4], [10, 8]]

def test_sq_mul_scalar():
    a = SQMatrix([[1, 2], [3, 4]])
    
    b = 2 * a
    assert b.data == [[2, 4], [6, 8]]
    
    c = a * 2
    assert c.data == [[2, 4], [6, 8]]

def test_sq_add_shape_error():
    a = SQMatrix([[1]])
    b = SQMatrix([[1, 2], [3, 4]])
    with pytest.raises(ValueError):
        _ = a + b

def test_sq_sub_shape_error():
    a = SQMatrix([[1]])
    b = SQMatrix([[1, 2], [3, 4]])
    with pytest.raises(ValueError):
        _ = a - b

def test_sq_mul_shape_error():
    a = SQMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = SQMatrix([[1, 2], [3, 4]])
    with pytest.raises(ValueError):
        _ = a * b

def test_sq_trace():
    a = SQMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert a.trace() == 15

# endregion

# region TRGMatrix tests

def test_trg_init_invalid():
    with pytest.raises(Exception):
        TRGMatrix([[1], [2, 3], [4, 5, 6]])

# endregion

# region UPTMatrix tests

def test_upt_init_valid():
    m = UPTMatrix([[1, 2], [3]])
    assert m.get_std_shape() == (2, 2)
    assert m.data == [[1, 2], [3]]

def test_upt_init_invalid():
    with pytest.raises(ValueError):
        UPTMatrix([[1], [2, 3]])

def test_upt_neg():
    m = -UPTMatrix([[1, 2], [3]])
    assert m.data == [[-1, -2], [-3]]

def test_upt_t():
    a = UPTMatrix([[1, 1], [1]])
    b = a.get_transpose()
    assert b.data == [[1, 0], [1, 1]]

def test_upt_add_matrix():
    a = UPTMatrix([[1, 2], [3]])
    b = UPTMatrix([[4, 5], [6]])
    c = a + b
    assert isinstance(c, UPTMatrix)
    assert c.data == [[5, 7], [9]]

    a = UPTMatrix([[1, 2], [3]])
    b = SQMatrix([[4, 5], [6, 7]])
    c = a + b
    assert isinstance(c, SQMatrix)
    assert c.data == [[5, 7], [9, 7]]

    a = UPTMatrix([[1, 2], [3]])
    b = STDMatrix([[4, 5], [6, 7]])
    c = a + b
    assert isinstance(c, SQMatrix)
    assert c.data == [[5, 7], [9, 7]]

def test_upt_add_scalar():
    a = UPTMatrix([[1, 2], [3]])
    b = a + 10
    assert isinstance(b, UPTMatrix)
    assert b.data == [[11, 12], [13]]

    c = 10 + a
    assert isinstance(c, UPTMatrix)
    assert c.data == [[11, 12], [13]]

def test_upt_sub_matrix():
    a = UPTMatrix([[5, 7], [9]])
    b = UPTMatrix([[1, 2], [3]])
    c = a - b
    assert isinstance(c, UPTMatrix)
    assert c.data == [[4, 5], [6]]

    a = UPTMatrix([[5, 7], [9]])
    b = SQMatrix([[1, 2], [3, 4]])
    c = a - b
    assert isinstance(c, SQMatrix)
    assert c.data == [[4, 5], [6, -4]]

    a = UPTMatrix([[5, 7], [9]])
    b = STDMatrix([[1, 2], [3, 4]])
    c = a - b
    assert isinstance(c, SQMatrix)
    assert c.data == [[4, 5], [6, -4]]

def test_upt_sub_scalar():
    a = UPTMatrix([[1, 2], [3]])
    b = a - 10
    assert isinstance(b, SQMatrix)
    assert b.data == [[-9, -8], [-7]]
    c = 10 - a
    assert isinstance(c, SQMatrix)
    assert c.data == [[9, 8], [7]]

def test_upt_mul_matrix():
    a = UPTMatrix([[1, 2], [3]])
    b = UPTMatrix([[1, 2], [3]])
    c = a * b
    assert isinstance(c, UPTMatrix)
    assert c.data == [[1, 8], [9]]

    a = UPTMatrix([[1, 2], [3]])
    b = SQMatrix([[1, 2], [0, 3]])
    c = a * b
    assert isinstance(c, SQMatrix)
    assert c.data == [[1, 8], [0, 9]]

    a = UPTMatrix([[1, 2], [3]])
    b = STDMatrix([[1, 2], [0, 3]])
    c = a * b
    assert isinstance(c, STDMatrix)
    assert c.data == [[1, 8], [0, 9]]

def test_upt_mul_scalar():
    a = UPTMatrix([[1, 2], [3]])
    b = a * 2
    assert isinstance(b, UPTMatrix)
    assert b.data == [[2, 4], [6]]
    c = 2 * a
    assert isinstance(c, UPTMatrix)
    assert c.data == [[2, 4], [6]]

def test_upt_add_shape_error():
    a = UPTMatrix([[1]])
    b = UPTMatrix([[1, 2], [3]])
    with pytest.raises(ValueError):
        _ = a + b

def test_upt_sub_shape_error():
    a = UPTMatrix([[1]])
    b = UPTMatrix([[1, 2], [3]])
    with pytest.raises(ValueError):
        _ = a - b

def test_upt_mul_shape_error():
    a = UPTMatrix([[1, 2, 3], [4, 5], [6]])
    b = UPTMatrix([[1, 2], [3]])
    with pytest.raises(ValueError):
        _ = a * b

def test_upt_trace():
    m = UPTMatrix([[1, 2], [3]])
    assert m.trace() == 4

# endregion

# region DWTMatrix tests

def test_dwt_init_valid():
    m = DWTMatrix([[1], [2, 3], [4, 5, 6]])
    assert m.get_std_shape() == (3, 3)
    assert m.data == [[1], [2, 3], [4, 5, 6]]

def test_dwt_init_invalid():
    with pytest.raises(ValueError):
        DWTMatrix([[1, 2], [3], [4, 5, 6]])  # Wrong lengths

def test_dwt_neg():
    m = -DWTMatrix([[1], [2, 3], [4, 5, 6]])
    assert m.data == [[-1], [-2, -3], [-4, -5, -6]]

def test_dwt_t():
    a = DWTMatrix([[1], [1, 1]])
    b = a.get_transpose()
    assert b.data == [[1, 1], [0, 1]]

def test_dwt_add_matrix():
    a = DWTMatrix([[1], [1, 1]])
    b = DWTMatrix([[1], [1, 1]])
    c = a + b
    assert isinstance(c, DWTMatrix)
    assert c.data == [[2], [2, 2]]

    a = DWTMatrix([[1], [1, 1]])
    b = SQMatrix([[1, 1], [1, 1]])
    c = a + b
    assert isinstance(c, SQMatrix)
    assert c.data == [[2, 1], [2, 2]]

    a = DWTMatrix([[1], [1, 1]])
    b = STDMatrix([[1, 1], [1, 1]])
    c = a + b
    assert isinstance(c, SQMatrix)
    assert c.data == [[2, 1], [2, 2]]

def test_dwt_add_scalar():
    a = DWTMatrix([[1], [2, 3], [4, 5, 6]])
    
    b = a + 10
    assert isinstance(b, DWTMatrix)
    assert b.data == [[11], [12, 13], [14, 15, 16]]
    
    c = 10 + a
    assert isinstance(c, DWTMatrix)
    assert c.data == [[11], [12, 13], [14, 15, 16]]

def test_dwt_sub_dwtmatrix():
    a = DWTMatrix([[7], [8, 9], [10, 11, 12]])
    b = DWTMatrix([[1], [2, 3], [4, 5, 6]])
    c = a - b
    assert isinstance(c, DWTMatrix)
    assert c.data == [[6], [6, 6], [6, 6, 6]]

    a = DWTMatrix([[7], [8, 9], [10, 11, 12]])
    b = SQMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    c = a - b
    assert isinstance(c, SQMatrix)
    assert c.data[0][0] == 6
    assert c.data[1][1] == 4
    assert c.data[2][2] == 3

    a = DWTMatrix([[7], [8, 9], [10, 11, 12]])
    b = STDMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    c = a - b
    assert isinstance(c, SQMatrix)
    assert c.data[0][0] == 6
    assert c.data[1][1] == 4
    assert c.data[2][2] == 3

def test_dwt_sub_scalar():
    a = DWTMatrix([[1], [2, 3], [4, 5, 6]])
    b = a - 10
    assert isinstance(b, DWTMatrix)
    assert b.data == [[-9], [-8, -7], [-6, -5, -4]]
    c = 10 - a
    assert isinstance(c, DWTMatrix)
    assert c.data == [[9], [8, 7], [6, 5, 4]]

def test_dwt_mul_dwtmatrix():
    a = DWTMatrix([[1], [2, 3]])
    b = DWTMatrix([[1], [2, 3]])
    c = a * b
    assert isinstance(c, DWTMatrix)
    assert c.data == [[1], [8, 9]]

    a = DWTMatrix([[1], [2, 3]])
    b = UPTMatrix([[1, 2], [3]])
    c = a * b
    assert isinstance(c, SQMatrix)
    assert c.data == [[1, 2], [2, 13]]

    a = DWTMatrix([[1], [2, 3]])
    b = SQMatrix([[1, 0], [2, 3]])
    c = a * b
    assert isinstance(c, SQMatrix)
    assert c.data == [[1, 0], [8, 9]]

    a = DWTMatrix([[1], [2, 3]])
    b = STDMatrix([[1, 0], [2, 3]])
    c = a * b
    assert isinstance(c, STDMatrix)
    assert c.data == [[1, 0], [8, 9]]

def test_dwt_mul_scalar():
    a = DWTMatrix([[1], [2, 3], [4, 5, 6]])
    b = a * 2
    assert isinstance(b, DWTMatrix)
    assert b.data == [[2], [4, 6], [8, 10, 12]]
    c = 2 * a
    assert isinstance(c, DWTMatrix)
    assert c.data == [[2], [4, 6], [8, 10, 12]]

def test_dwt_add_shape_error():
    a = DWTMatrix([[1], [2, 3], [4, 5, 6]])
    b = DWTMatrix([[1], [2, 3]])
    with pytest.raises(ValueError):
        _ = a + b

def test_dwt_sub_shape_error():
    a = DWTMatrix([[1], [2, 3], [4, 5, 6]])
    b = DWTMatrix([[1], [2, 3]])
    with pytest.raises(ValueError):
        _ = a - b

def test_dwt_mul_shape_error():
    a = DWTMatrix([[1], [2, 3], [4, 5, 6]])
    b = DWTMatrix([[1], [2, 3]])
    with pytest.raises(ValueError):
        _ = a * b

def test_dwt_trace():
    m = DWTMatrix([[1], [2, 3]])
    assert m.trace() == 4

# endregion

# region DIGMatrix tests

def test_dig_init_valid():
    m = DIGMatrix([1, 2, 3])
    assert m.get_std_shape() == (3, 3)
    assert m.data == [1, 2, 3]

def test_dig_neg():
    m = DIGMatrix([1, -2, 3])
    neg = -m
    assert isinstance(neg, DIGMatrix)
    assert neg.data == [-1, 2, -3]

def test_dig_t():
    a = DIGMatrix([1, 2, 3])
    b = a.get_transpose()
    assert b.data == a.data

def test_dig_add_matrix():
    a = DIGMatrix([1, 2, 3])
    b = DIGMatrix([4, 5, 6])
    c = a + b
    assert isinstance(c, DIGMatrix)
    assert c.data == [5, 7, 9]

    a = DIGMatrix([1, 1])
    b = DWTMatrix([[1], [1, 1]])
    c = a + b
    assert isinstance(c, SQMatrix)
    assert c.data == [[2], [1, 2]]

    a = DIGMatrix([1, 1])
    b = UPTMatrix([[1, 1], [1]])
    c = a + b
    assert isinstance(c, UPTMatrix)
    assert c.data == [[2, 1], [2]]

    a = DIGMatrix([1, 1])
    b = SQMatrix([[1, 1], [1, 1]])
    c = a + b
    assert isinstance(c, SQMatrix)
    assert c.data == [[2, 1], [1, 2]]

    a = DIGMatrix([1, 1])
    b = STDMatrix([[1, 1], [1, 1]])
    c = a + b
    assert isinstance(c, SQMatrix)
    assert c.data == [[2, 1], [1, 2]]

def test_dig_add_scalar():
    m = DIGMatrix([1, 2, 3])
    result = m + 5
    assert isinstance(result, DIGMatrix)
    assert result.data == [6, 7, 8]
    
    result2 = 5 + m
    assert result2.data == [6, 7, 8]

def test_dig_sub_scalar():
    m = DIGMatrix([1, 2, 3])
    
    c = m - 1
    assert isinstance(c, DIGMatrix)
    assert c.data == [0, 1, 2]
    
    c = 10 - m
    assert isinstance(c, DIGMatrix)
    assert c.data == [9, 8, 7]

def test_dig_sub_matrix():
    a = DIGMatrix([7, 8, 9])
    b = DIGMatrix([1, 2, 3])
    c = a - b
    assert isinstance(c, DIGMatrix)
    assert c.data == [6, 6, 6]

    a = DIGMatrix([2, 2])
    b = DWTMatrix([[1], [1, 1]])
    c = a - b
    assert isinstance(c, SQMatrix)
    assert c.data == [[1], [-1, 1]]

    a = DIGMatrix([2, 2])
    b = UPTMatrix([[1, 1], [1]])
    c = a - b
    assert isinstance(c, UPTMatrix)
    assert c.data == [[1, -1], [1]]

    a = DIGMatrix([2, 2])
    b = SQMatrix([[1, 1], [1, 1]])
    c = a - b
    assert isinstance(c, SQMatrix)
    assert c.data == [[1, -1], [-1, 1]]

    a = DIGMatrix([2, 2])
    b = STDMatrix([[1, 1], [1, 1]])
    c = a - b
    assert isinstance(c, SQMatrix)
    assert c.data == [[1, -1], [-1, 1]]

def test_dig_mul_scalar():
    a = DIGMatrix([1, 2, 3])
    b = a * 2
    assert isinstance(b, DIGMatrix)
    assert b.data == [2, 4, 6]
    c = 2 * a
    assert c.data == [2, 4, 6]

def test_dig_mul_matrix():
    a = DIGMatrix([1, 1, 1])
    b = DIGMatrix([1, 1, 1])
    c = a * b
    assert isinstance(c, DIGMatrix)
    assert c.data == [1, 1, 1]

    a = DIGMatrix([1, 1])
    b = DWTMatrix([[1], [1, 1]])
    c = a * b
    assert isinstance(c, DWTMatrix)
    assert c.data == [[1], [1, 1]]

    a = DIGMatrix([1, 1])
    b = UPTMatrix([[1, 1], [1]])
    c = a * b
    assert isinstance(c, UPTMatrix)
    assert c.data == [[1, 1], [1]]

    a = DIGMatrix([1, 1])
    b = SQMatrix([[1, 1], [1, 1]])
    c = a * b
    assert isinstance(c, SQMatrix)
    assert c.data == [[1, 1], [1, 1]]

    a = DIGMatrix([1, 1])
    b = STDMatrix([[1, 1], [1, 1]])
    c = a * b
    assert isinstance(c, STDMatrix)
    assert c.data == [[1, 1], [1, 1]]

def test_dig_shape_error():
    a = DIGMatrix([1, 2, 3])
    b = DIGMatrix([4, 5])
    with pytest.raises(ValueError):
        _ = a + b
    with pytest.raises(ValueError):
        _ = a - b
    with pytest.raises(ValueError):
        _ = a * b

# endregion 

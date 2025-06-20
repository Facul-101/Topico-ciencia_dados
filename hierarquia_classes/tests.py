import pytest
from my_array import Array
from my_singly_linked_list import SinglyLinkedList
from my_stack import Stack
from my_doubly_linked_list import DoublyLinkedList
from my_queue import Queue

# region ARRAY

def test_array_init_and_type():
    arr = Array(int, capacity=3)
    assert arr._type is int
    assert arr._capacity == 3
    assert arr.is_empty()

def test_insert_and_len():
    arr = Array(int, capacity=3)
    arr.insert_end(1)
    arr.insert_end(2)
    arr.insert_beginning(0)
    assert len(arr) == 3
    assert arr[0] == 0
    assert arr[1] == 1
    assert arr[2] == 2

def test_insert_by_key_and_setitem():
    arr = Array(int, capacity=5)
    arr.insert_end(1)
    arr.insert_end(2)
    arr.insert_by_index(10, 1)
    assert arr[1] == 10
    arr[1] = 20
    assert arr[1] == 20

def test_type_check():
    arr = Array(int, capacity=2)
    with pytest.raises(ValueError):
        arr.insert_end("not an int")

def test_remove_methods():
    arr = Array(int, capacity=3)
    arr.insert_end(1)
    arr.insert_end(2)
    arr.insert_end(3)
    arr.remove_beginning()
    arr.remove_end()
    assert len(arr) == 1
    assert arr[0] == 2
    arr.insert_end(4)
    arr.remove_by_index(0)
    assert len(arr) == 1
    assert arr[0] == 4

def test_get_methods():
    arr = Array(int, capacity=3)
    arr.insert_end(5)
    arr.insert_end(6)
    arr.insert_end(7)
    assert arr.get_beginning_item() == 5
    assert arr.get_end_item() == 7
    assert arr.get_index_item(1) == 6

def test_is_full_and_grow():
    arr = Array(int, capacity=2, dynamic=True)
    arr.insert_end(1)
    arr.insert_end(2)
    assert arr.is_full()
    arr.insert_end(3)
    assert arr._capacity >= 3
    assert len(arr) == 3

def test_index_error():
    arr = Array(int, capacity=2)
    arr.insert_end(1)
    with pytest.raises(IndexError):
        arr.get_index_item(5)
    with pytest.raises(IndexError):
        arr.remove_by_index(2)

def test_iteration():
    arr = Array(int, capacity=3)
    arr.insert_end(1)
    arr.insert_end(2)
    arr.insert_end(3)
    assert list(arr) == [1, 2, 3]

# endregion

# region SINGLY LINKED LIST

def test_sll_init_and_empty():
    sll = SinglyLinkedList()
    assert sll.is_empty()
    assert sll._size == 0
    assert sll.head is None

def test_sll_insert_and_len():
    sll = SinglyLinkedList()
    sll.insert_end(1)
    sll.insert_end(2)
    sll.insert_beginning(0)
    assert sll._size == 3
    assert sll[0] == 0
    assert sll[1] == 1
    assert sll[2] == 2

def test_sll_insert_by_index_and_setitem():
    sll = SinglyLinkedList()
    sll.insert_end(1)
    sll.insert_end(2)
    sll.insert_by_index(10, 1)
    assert len(sll) == 3
    assert sll[1] == 10
    sll[1] = 20
    assert sll[1] == 20

    sll = SinglyLinkedList()
    sll.insert_end(1)
    sll.insert_end(2)
    sll.insert_end(3)
    sll.insert_by_index(10, 1)
    assert sll[1] == 10
    print(list(sll))

def test_sll_pop_methods():
    sll = SinglyLinkedList()
    sll.insert_end(1)
    sll.insert_end(2)
    sll.insert_end(3)
    sll.remove_beginning()
    assert sll[0] == 2
    sll.remove_end()
    assert sll._size == 1
    sll.insert_end(4)
    sll.remove_by_index(0)
    assert sll[0] == 4

def test_sll_get_methods():
    sll = SinglyLinkedList()
    sll.insert_end(5)
    sll.insert_end(6)
    sll.insert_end(7)
    assert sll.get_beginning_item() == 5
    assert sll.get_end_item() == 7
    assert sll.get_index_item(1) == 6

def test_sll_index_error():
    sll = SinglyLinkedList()
    sll.insert_end(1)
    import pytest
    with pytest.raises(IndexError):
        sll.get_index_item(5)
    with pytest.raises(IndexError):
        sll.remove_by_index(2)
    with pytest.raises(IndexError):
        SinglyLinkedList().remove_beginning()

def test_sll_iteration():
    sll = SinglyLinkedList()
    sll.insert_end(1)
    sll.insert_end(2)
    sll.insert_end(3)
    assert list(sll) == [1, 2, 3]

# endregion

# region STACK

def test_stack_init_and_empty():
    stack = Stack(int, 3)
    assert stack.is_empty()
    assert len(stack) == 0
    assert stack._capacity == 3
    assert stack._type is int

def test_stack_push_and_len():
    stack = Stack(int, 2)
    stack.push(1)
    assert not stack.is_empty()
    assert len(stack) == 1
    stack.push(2)
    assert len(stack) == 2

def test_stack_push_type_error():
    stack = Stack(int, 2)
    with pytest.raises(ValueError):
        stack.push("not an int")

def test_stack_overflow():
    stack = Stack(int, 1)
    stack.push(1)
    with pytest.raises(MemoryError):
        stack.push(2)

def test_stack_pop_and_underflow():
    stack = Stack(int, 2)
    stack.push(10)
    assert stack.pop() == 10
    with pytest.raises(MemoryError):
        stack.pop()

def test_stack_swap():
    stack = Stack(int, 3)
    stack.push(1)
    stack.push(2)
    stack.swap()
    assert stack.pop() == 1
    assert stack.pop() == 2

# endregion

# region DOUBLY LINKED LIST

def test_dll_init_and_empty():
    dll = DoublyLinkedList()
    assert dll.is_empty()
    assert dll._size == 0
    assert dll.head is None

def test_dll_insert_and_len():
    dll = DoublyLinkedList()
    dll.insert_end(1)
    dll.insert_end(2)
    dll.insert_beginning(0)
    assert len(dll) == 3
    assert dll.head.value == 0              # type: ignore
    assert dll.head.next.value == 1         # type: ignore
    assert dll.head.next.next.value == 2    # type: ignore

def test_dll_insert_by_index():
    dll = DoublyLinkedList()
    dll.insert_end(1)
    dll.insert_end(3)
    dll.insert_by_index(2, 1)
    assert dll.head.value == 1              # type: ignore
    assert dll.head.next.value == 2         # type: ignore
    assert dll.head.next.next.value == 3    # type: ignore

def test_dll_remove_beginning():
    dll = DoublyLinkedList()
    dll.insert_end(1)
    dll.insert_end(2)
    dll.remove_beginning()
    assert dll.head.value == 2  # type: ignore
    assert dll._size == 1

def test_dll_remove_by_index():
    dll = DoublyLinkedList()
    dll.insert_end(1)
    dll.insert_end(2)
    dll.insert_end(3)
    dll.remove_by_index(1)
    assert dll.head.value == 1          # type: ignore
    assert dll.head.next.value == 3     # type: ignore
    assert len(dll) == 2

def test_dll_remove_beginning_empty():
    dll = DoublyLinkedList()
    with pytest.raises(IndexError):
        dll.remove_beginning()

def test_dll_remove_by_index_out_of_bounds():
    dll = DoublyLinkedList()
    dll.insert_end(1)
    with pytest.raises(IndexError):
        dll.remove_by_index(2)

# endregion

# region QUEUE

def test_queue_init_and_empty():
    queue = Queue(int, 3)
    assert queue.is_empty()
    assert len(queue) == 0
    assert queue._capacity == 3
    assert queue._type is int

def test_queue_insert_and_len():
    queue = Queue(int, 2)
    queue.insert(1)
    assert not queue.is_empty()
    assert len(queue) == 1
    queue.insert(2)
    assert len(queue) == 2

def test_queue_insert_type_error():
    queue = Queue(int, 2)
    with pytest.raises(ValueError):
        queue.insert("not an int")

def test_queue_overflow():
    queue = Queue(int, 1)
    queue.insert(1)
    with pytest.raises(MemoryError):
        queue.insert(2)

def test_queue_pop_and_underflow():
    queue = Queue(int, 5)
    queue.insert(10)
    assert queue.pop() == 10
    with pytest.raises(MemoryError):
        queue.pop()

def test_queue_fifo_order():
    queue = Queue(int, 3)
    queue.insert(1)
    queue.insert(2)
    queue.insert(3)
    assert queue.pop() == 1
    assert queue.pop() == 2
    assert queue.pop() == 3

def test_queue_swap():
    queue = Queue(int, 4)
    queue.insert(1)
    queue.insert(2)
    queue.insert(3)
    queue.insert(4)
    queue.swap()
    assert queue.pop() == 2
    assert queue.pop() == 1
    assert queue.pop() == 3
    assert queue.pop() == 4

# endregion
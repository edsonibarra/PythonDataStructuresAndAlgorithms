import pytest
from src.data_structures.singly_linked_list.linked_list import LinkedList


@pytest.fixture
def populated_linked_list():
    linked_list = LinkedList()
    for n in range(1, 5):
        linked_list.append(n)
    return linked_list


@pytest.fixture
def empty_linked_list():
    return LinkedList()


def test_linked_list_creation(empty_linked_list):
    linked_list = empty_linked_list
    assert isinstance(linked_list, LinkedList)


def test_empty_linked_list_not_printing_values():
    linked_list = LinkedList()
    assert linked_list.print_list() == LinkedList.EMPTY_LINKED_LIST_MSG


def test_linked_list_insertion_append():
    linked_list = LinkedList()
    linked_list.append(1)
    assert linked_list.head.data == 1
    linked_list.append(2)
    assert linked_list.head.next.data == 2
    

def test_linked_list_tail(populated_linked_list):
    linked_list = populated_linked_list
    assert linked_list.tail.data == 4

def test_linked_list_tail_head_when_len_1(empty_linked_list):
    linked_list = empty_linked_list

    assert linked_list.head is None
    assert linked_list.tail is None

    linked_list.append(1)

    assert linked_list.head is linked_list.tail
    assert linked_list.head.data == linked_list.tail.data


def test_linked_list_tail_head_are_moving_correctly(empty_linked_list):
    linked_list = empty_linked_list

    assert linked_list.head is None
    assert linked_list.tail is None

    linked_list.append(1)

    assert linked_list.head is linked_list.tail
    assert linked_list.head.data == linked_list.tail.data

    linked_list.prepend(0)

    assert linked_list.head.data == 0
    assert linked_list.head is not linked_list.tail
    assert linked_list.tail.data == 1
    assert linked_list.head.next is linked_list.tail
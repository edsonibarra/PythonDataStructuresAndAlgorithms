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


def test_linked_list_length(empty_linked_list, populated_linked_list):
    empty_ll = empty_linked_list
    pop_ll = populated_linked_list

    assert len(empty_ll) == 0
    assert len(pop_ll) == 4

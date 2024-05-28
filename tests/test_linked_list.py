from linked_list.linked_list import StackLinkedList, QueueLinkedList
import pytest

def test_stack_linked_list():
    s = StackLinkedList()
    assert s.is_empty()
    with pytest.raises(Exception):
        s.pop()
    s.push('A')
    s.push('B')
    assert len(s) == 2
    assert not s.is_empty()
    assert s.top() == 'B'
    assert s.pop() == 'B'
    assert s.pop() == 'A'
    assert s.is_empty()
    
    
def test_queue_linked_list():
    s = QueueLinkedList()
    assert s.is_empty()
    with pytest.raises(Exception):
        s.dequeue()
    s.enqueue('A')
    s.enqueue('B')
    assert len(s) == 2
    assert not s.is_empty()
    assert s.first() == 'A'
    assert s.dequeue() == 'A'
    assert s.dequeue() == 'B'
    assert s.is_empty()

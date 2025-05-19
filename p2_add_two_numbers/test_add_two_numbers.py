# p2_add_two_numbers/test_add_two_numbers.py

import pytest
from p2_add_two_numbers.add_two_numbers import Solution, ListNode

def build_linked_list(values: list[int]) -> ListNode | None:
    """Вспомогательная функция: из списка цифр делает связный список."""
    dummy = ListNode(0)
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next

def linked_list_to_list(node: ListNode | None) -> list[int]:
    """Вспомогательная функция: из связного списка делает обычный список."""
    result: list[int] = []
    while node:
        result.append(node.val)
        node = node.next
    return result

@pytest.mark.parametrize(
    "a,b,expected",
    [
        # Примеры из условия
        ([2,4,3], [5,6,4], [7,0,8]),
        ([0],     [0],     [0]),
        ([9,9,9], [1],     [0,0,0,1]),

        # Разная длина списков
        ([1,2],   [9],     [0,3]),       # 21 + 9 = 30
        ([5],     [5],     [0,1]),       # перенос в конец

        # Один список длиннее
        ([2,1,3], [5,4],   [7,5,3]),     # 312 + 45 = 357

        # Кейс большого переноса
        ([9,9],   [9,9],   [8,9,1]),     # 99 + 99 = 198
    ]
)
def test_add_two_numbers(a: list[int], b: list[int], expected: list[int]):
    sol = Solution()
    l1 = build_linked_list(a)
    l2 = build_linked_list(b)
    result = sol.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == expected

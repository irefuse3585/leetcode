from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    @staticmethod
    def build_linked_list(values: list[int]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        for v in values:
            node = ListNode(v)
            tail.next = node
            tail = node
        return dummy.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = 0
        sum2 = 0
        i = 0
        while l1 is not None or l2 is not None:
            if l1 is not None:
                sum1 += l1.val * pow(10, i)
                l1 = l1.next
            if l2 is not None:
                sum2 += l2.val * pow(10, i)
                l2 = l2.next
            i += 1
        total = sum1 + sum2
        final = []
        if total == 0:
            final.append(0)
        while total != 0:
            final.append(total % 10)
            total //= 10
        return Solution.build_linked_list(final)
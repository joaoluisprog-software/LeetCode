# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        n1 = 0
        n2 = 0

        # Transform l1 in number
        current = l1
        multiplier = 1

        while current:
            n1 += current.val * multiplier
            multiplier *= 10
            current = current.next

        # Transform l2 in number
        current = l2
        multiplier = 1

        while current:
            n2 += current.val * multiplier
            multiplier *= 10
            current = current.next

        total = n1 + n2

        # Create a linked list with the result
        dummy = ListNode(0)
        current = dummy

        if total == 0:
            return dummy

        while total > 0:
            digit = total % 10
            total //= 10

            current.next = ListNode(digit)
            current = current.next

        return dummy.next
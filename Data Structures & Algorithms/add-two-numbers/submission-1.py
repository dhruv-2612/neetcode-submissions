# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1.val == 0:
            return l2
        if l2.val == 0:
            return l1
        
        res = ListNode()
        tmp = res
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            tmp.next = ListNode(total%10)
            carry = total//10
            tmp = tmp.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res.next

        

        
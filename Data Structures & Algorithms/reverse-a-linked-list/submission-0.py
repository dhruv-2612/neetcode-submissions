# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        n1=None
        n2=head
        while n2!=None:
            # n2, n2.next, n1 = n2.next, n1, n2
            n1, n2.next, n2 = n2, n1, n2.next
        return n1
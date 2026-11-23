# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None:
            return
        slow = head
        fast = head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        temp = slow.next
        slow.next = None
        tail=None
        while temp:
            temp.next, temp, tail = tail, temp.next, temp
            # n1, n2.next, n2 = n2, n1, n2.next
        temp=head
        while tail != None:
             temp.next, tail.next, tail, temp = tail, temp.next, tail.next, temp.next 

    # def nextNode(self, curr: Optional[ListNode], cnt: int) -> Optional[ListNode]:
    #     if cnt == 0:
    #         temp, curr.next = curr.next, None
    #         return temp
    #     temp = self.nextNode(curr.next, cnt-1)
    #     temp2 = None
    #     if temp:
    #         temp2 = temp.next
    #     temp.next, curr.next = curr.next, temp
    #     return temp2


        
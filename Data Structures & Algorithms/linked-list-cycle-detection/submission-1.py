# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        temp1= head
        temp2= head.next
        while temp1 != temp2 and temp1 != temp2.next:
            temp1 = temp1.next
            if temp2 and temp2.next != None and temp2.next.next != None:
                temp2 = temp2.next.next
            else:
                return False
        return True


        
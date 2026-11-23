# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None or n==0:
            return head
        cnt=1
        slow=head
        fast=head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            cnt+=1
        print(cnt)
        size = 2*cnt
        if fast == None:
            size-=1
        if n==size:
            return head.next
        pos=size-n
        if pos>=cnt:
            while cnt<pos:
                slow=slow.next
                cnt+=1
            slow.next=slow.next.next
        else:
            pos-=1
            cnt=0
            slow=head
            while cnt<pos:
                slow=slow.next
                cnt+=1
            slow.next = slow.next.next
        return head


        
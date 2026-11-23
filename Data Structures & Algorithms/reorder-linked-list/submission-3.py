# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None:
            return 
        tmp=head
        cnt=0
        while tmp!= None:
            cnt+=1
            tmp=tmp.next
        

        def rec(root:Optional[ListNode], n: int, flag: bool):
            if n==1:
                if flag:
                    tmp, root.next = root.next, None
                    return tmp
                else:
                    tmp, root.next.next = root.next.next, None
                    return tmp
            tmp = rec(root.next, n-1, flag)
            root.next, tmp.next, tmp = tmp, root.next, tmp.next
            return tmp 
        
        rec(head, math.ceil(cnt/2), cnt%2==1)


   

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        

        n=len(lists)
        while len(lists)>1:
            tmp=0
            newLists = []
            while tmp<(len(lists)-1):
                newLists.append(self.mergeTwoLists(lists[tmp], lists[tmp+1]))
                tmp+=2
            if tmp<len(lists):
                newLists.append(lists[tmp])
            lists = newLists
        return lists[0]



    def mergeTwoLists(self, l1:Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        merge = res
        while l1 and l2:
            if l1.val < l2.val:
                merge.next = l1
                merge = merge.next
                l1 = l1.next
            else:
                merge.next = l2
                merge = merge.next
                l2 = l2.next
        tmp = l1 if l1 else l2
        while tmp:
            merge.next = tmp
            merge = merge.next
            tmp = tmp.next
        return res.next
        
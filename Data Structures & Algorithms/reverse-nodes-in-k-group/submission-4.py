# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        start = curr
        prevEnd = None
        flag = True
        while curr:
            # print(curr.val)
            cnt=0
            while cnt<k and curr:
                cnt+=1
                curr = curr.next
            if(cnt==k):
                newL = self.reverseK(start, k)
                if prevEnd:
                    prevEnd.next = newL
                # print(start.val)
                start, prevEnd = curr, start
                if flag:
                    head = newL
                    flag = False
                # self.printList(head)
            else:
                prevEnd.next = start if prevEnd else None
                break
        return head
            

    def printList(self, head) -> None:
        temp = head
        strl = ""
        while temp!=None:
            strl+= " " + str(temp.val)
            temp = temp.next
        print(strl)

    def reverseK(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tmp = None
        cnt = 0
        while cnt<k:
            cnt+=1
            tmp, head.next, head = head, tmp, head.next
        # self.printList(tmp)
        return tmp



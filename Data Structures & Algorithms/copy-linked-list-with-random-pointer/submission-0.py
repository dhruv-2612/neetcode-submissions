"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        nMap = {}        
        
        def rec(head: Optional[Node]) -> Optional[Node]:
            if head == None:
                return None
            temp = Node(head.val)
            nMap[head] = temp
            temp.next = rec(head.next)
            if head.random == None:
                temp.random = None
            else:
                temp.random = nMap[head.random]
            return temp
        newHead = rec(head)
        return newHead
            



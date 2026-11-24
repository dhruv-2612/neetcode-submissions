class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.keyMap = {}
        self.nodeMap = {}
        self.head = ListNode()
        self.cap = capacity
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def printList(self) -> None:
        temp = self.head
        strl = ""
        while temp!=None:
            strl+= " " + str(temp.val)
            temp = temp.next
        print(strl)

    def get(self, key: int) -> int:
        # print("get", key)
        # self.printList()
        if(key in self.keyMap):
            tmp = self.nodeMap[key]
            tmp.prev.next, tmp.next.prev = tmp.next, tmp.prev
            self.tail.prev.next, self.tail.prev, tmp.prev, tmp.next = tmp, tmp, self.tail.prev, self.tail
            return self.keyMap[key]
        else:
            return -1


        

    def put(self, key: int, value: int) -> None:
        # print("put", key, value)
        if(key in self.keyMap):
            self.keyMap[key] = value
            tmp = self.nodeMap[key]
            tmp.prev.next, tmp.next.prev = tmp.next, tmp.prev
            self.tail.prev.next, self.tail.prev, tmp.prev, tmp.next = tmp, tmp, self.tail.prev, self.tail
        else:
            # print(self.ll.val)
            if(len(self.keyMap) == self.cap):
                del self.keyMap[self.head.next.val]
                del self.nodeMap[self.head.next.val]
                self.head.next.next.prev = self.head
                self.head.next = self.head.next.next
            self.keyMap[key] = value
            newNode = ListNode(key)
            self.nodeMap[key] = newNode
            tmp = self.tail.prev
            tmp.next, newNode.prev, newNode.next, self.tail.prev = newNode, tmp, self.tail, newNode
        # self.printList()
        
    
    

            



    
        

class MinStack:

    def __init__(self):
        self.stc = []
        self.min = float('-inf')

    def push(self, val: int) -> None:
        if self.stc:
            self.stc.append(val-self.min)
            self.min = val if val<self.min else self.min
        else:
            self.stc.append(0)
            self.min = val
        # print("push",self.stc)

    def pop(self) -> None:
        pop = self.stc.pop()

        if pop < 0:
            self.min-=pop
        # print("pop",self.stc)
        
        

    def top(self) -> int:
        # print("top", self.stc)
        if not self.stc:
            return None

        top = self.stc[-1]
        if top > 0:
            return top+self.min
        else:
            return self.min
        

    def getMin(self) -> int:
        # print("min", self.stc)
        return self.min
        

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if piles == []:
            return 0
        mx=piles[0]
        t=0
        for pile in piles:
            t+=pile
            mx=max(mx, pile)
        mn=math.ceil(t/h)
        mid=int((mn+mx)/2)
        while mn<mx:
            hrs=self.getHours(piles, mid)
            if hrs>h:
                mn=mid+1
            else:
                mx=mid
            mid=int((mn+mx)/2)
        return mx


    def getHours(self, piles: List[int], spd: int):
        res=0
        for pile in piles:
            res+=math.ceil(pile/spd)
        return res        
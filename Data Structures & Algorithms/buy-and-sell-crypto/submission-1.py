class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        back = [prices[-1]] * len(prices)
        for i in range(len(prices)-2, -1, -1):
            back[i] = max(back[i+1], prices[i])
        res=0
        for i in range(len(prices)):
            res = max(res, back[i]-prices[i])
        return res


        
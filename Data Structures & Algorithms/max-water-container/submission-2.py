class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        res=0
        while(l<r):
            res = max((min(heights[l], heights[r]) * (r-l)), res)
            while(heights[r]<heights[l] and l<r):
                r-=1
                res = max((min(heights[l], heights[r]) * (r-l)), res)
                # print(heights[l], heights[r])
            l+=1
        return res

        
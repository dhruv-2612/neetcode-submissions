class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if(heights == []):
            return 0

        stc = [-1]
        res = 0
        for i in range(len(heights)):
            if stc[-1] == -1 or heights[stc[-1]] <= heights[i]:
                stc.append(i)
            else:
                while(stc[-1] != -1 and heights[stc[-1]] > heights[i]):
                    pop = stc.pop()
                    st = stc[-1]
                    res = max(res, (i-st-1)*heights[pop])
                stc.append(i)
        while stc[-1] != -1:
            pop = stc.pop()
            st = stc[-1]
            res = max(res, (len(heights)-st-1)*heights[pop])
        
        return res


        
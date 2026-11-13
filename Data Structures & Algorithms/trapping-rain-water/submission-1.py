class Solution:
    def trap(self, height: List[int]) -> int:
        m = height[-1]
        back = [height[-1]] * len(height)
        for i in range(len(height)-1, -1, -1):
            back[i] = max(m, height[i])
            m = max(m, height[i])
        st=0
        res=0
        while(st<len(height)-1):
            en=st+1
            while(en<len(height) and height[en]<height[st]):
                res+=min(back[en], height[st])-height[en]
                en+=1
            st=en
        return res

        
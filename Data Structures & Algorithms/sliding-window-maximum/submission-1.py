class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r=k-1
        maxi = 0
        for i in range(0, k):
            if nums[i]>=nums[maxi]:
                maxi=i
        res = []
        for r in range(k-1, len(nums)):
            if nums[r] >= nums[maxi]:
                maxi = r
            if maxi >= r-k+1:
                res.append(nums[maxi])
            else:
                maxi=r-k+1
                for i in range(r-k+1, r+1):
                    if nums[i]>=nums[maxi]:
                        maxi=i
                res.append(nums[maxi])
            
        return res
        
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)<3:
            return min(nums)
        if nums[0]<nums[-1]:
            return nums[0]
        st=0
        en=len(nums)-1
        mid=int((st+en)/2)
        while(nums[st]>nums[en]):
            if(nums[mid-1]>nums[mid]<nums[mid+1]):
                return nums[mid]
            elif(nums[st]<=nums[mid]>=nums[en]):
                st=mid+1
            elif(nums[st]>=nums[mid]<=nums[en]):
                en=mid-1
            mid=int((st+en)/2)
        return nums[st]
            


        
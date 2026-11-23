class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow, fast =  nums[slow], nums[nums[fast]]
            if (fast == slow):
                break
        fast = 0
        while True:
            slow, fast = nums[slow], nums[fast]
            if (fast == slow):
                return slow



        
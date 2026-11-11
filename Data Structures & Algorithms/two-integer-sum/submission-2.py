class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        for i in range(len(nums)):
            pos[nums[i]] = i
        for i in range(len(nums)):
            if ((pos.get(target-nums[i], -1) != -1) & (pos.get(target-nums[i], -1) != i)):
                return [i, pos.get(target-nums[i])]
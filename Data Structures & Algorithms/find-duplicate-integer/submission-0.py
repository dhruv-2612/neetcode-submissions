class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num = nums[0]
        while True:
            # print(num, nums)
            if nums[num] == -1:
                return num
            else:
                nums[num], num = -1, nums[num]


        
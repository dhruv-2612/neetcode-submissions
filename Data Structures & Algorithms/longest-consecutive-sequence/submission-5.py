class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        master = set(nums)
        length=0
        for num in nums:
            if num-1 not in master:
                temp_len=1
                while(num+1 in master):
                    num+=1
                    temp_len+=1
                length=max(length, temp_len)
        return length
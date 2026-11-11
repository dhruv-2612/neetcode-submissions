from collections import Counter


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for i,cnt in count.items():
            if(cnt > 1):
                return  True
        return False
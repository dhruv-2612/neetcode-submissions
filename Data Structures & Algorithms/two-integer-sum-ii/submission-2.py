class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = {}
        sol=[0,0]
        for i in range(len(numbers)):
            if numbers[i] not in nums:
                nums[numbers[i]] = i+1
        for num in numbers:
            if num == target-num and numbers[nums.get(num)] == num:
                sol[0] = nums.get(num)
                sol[1] = sol[0]+1
            elif num <= target//2 and (target-num) in nums:
                sol[0] = nums.get(num)
                sol[1] = nums.get(target-num)
                break
        return sol

        
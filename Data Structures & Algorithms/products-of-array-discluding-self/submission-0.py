class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [num for num in nums]
        backward = [num for num in nums]
        for i in range(1, len(nums), 1):
            forward[i] = forward[i-1]*nums[i]
        for i in range(len(nums)-2, 0, -1 ):
            backward[i] = backward[i+1]*nums[i]
        forward[-1] = 1
        backward[0] = 1
        res = []
        res.append(backward[1])
        for i in range(1, len(nums)-1, 1):
            res.append(forward[i-1]*backward[i+1])
        res.append(forward[-2])
        return res


        
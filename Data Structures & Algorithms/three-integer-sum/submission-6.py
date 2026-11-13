class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)
        nums_2 = []
        for num in nums:
            if num not in count:
                nums_2.append(num)
            count[num] += 1
        nums_2 = sorted(nums_2)
        sol = []
        if count[0]>2:
            sol.append([0,0,0])
        for i in range(len(nums_2)):
            count[nums_2[i]] -=1
            for j in range(i+1, len(nums_2)):
                count[nums_2[j]] -=1
                temp = -(nums_2[i] + nums_2[j])
                if temp in count and count[temp]>0:
                    item = sorted([nums_2[i], nums_2[j], temp])
                    if item not in sol:
                        sol.append(item)
                count[nums_2[j]] +=1
            count[nums_2[i]] +=1    
        return sol
            
        
        
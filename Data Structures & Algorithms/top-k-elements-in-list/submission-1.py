class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        freq = {1:[]}
        n = len(nums)
        max_freq = 1
        result = []
        for num in nums:
            if num in numbers:
                freq[numbers[num]].remove(num)
                numbers[num]+=1
                if numbers[num] > max_freq:
                    max_freq=numbers[num]
                    freq[numbers[num]] = []
                freq[numbers[num]].append(num)
            else:
                numbers[num] = 1
                freq[1].append(num)
        while k>0:
            result.extend(freq[max_freq])
            k-= len(freq[max_freq])
            max_freq-=1

        return result

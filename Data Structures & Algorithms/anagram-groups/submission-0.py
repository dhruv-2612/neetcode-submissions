from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        while len(strs) > 0:
            temp = []
            temp.append(strs[0])
            cnt = Counter(strs[0])
            for i in range(len(strs)-1):
                if (Counter(strs[i+1]) == cnt):
                    temp.append(strs[i+1])
            result.append(temp)
            for t in temp:
                strs.remove(t)
        return result
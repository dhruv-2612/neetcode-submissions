class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l=0
        r=0
        char = [False] * 256
        while r<len(s):
            # print(s[l])
            while r<len(s) and char[ord(s[r])] == False:
                char[ord(s[r])] = True
                r+=1
            res = max((r-l), res)
            while r<len(s) and ord(s[l]) != ord(s[r]):
                char[ord(s[l])] = False
                l+=1
            l+=1
            r+=1
        return res
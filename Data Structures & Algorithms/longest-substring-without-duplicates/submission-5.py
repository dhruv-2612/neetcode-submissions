class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        ptr=0
        substr = ""
        l=len(s)
        while ptr<l:
            # print(s[l])
            while ptr<l and s[ptr] not in substr:
                substr+=s[ptr]
                ptr+=1
            res = max(len(substr), res)
            while ptr<l and s[ptr] in substr:
                substr = substr[1:]
            if ptr<l:
                substr+=s[ptr]
                ptr+=1
        return res
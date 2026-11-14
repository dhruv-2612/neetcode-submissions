class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        res=0
        maxf=1
        count = [0] * 26
        while r<len(s):
            while r<len(s):
                count[ord(s[r])-ord('A')]+=1
                maxf = max(count[ord(s[r])-ord('A')], maxf)
                if (r-l+1-maxf)>k:
                    break
                res = max(res, (r-l+1))
                r+=1
            while (r-l+1-maxf)>k:
                count[ord(s[l])-ord('A')]-=1
                l+=1
            r+=1
            
        return res
        
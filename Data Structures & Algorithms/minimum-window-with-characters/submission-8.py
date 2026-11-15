class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t in s:
            return t
        if len(s) < len(t):
            return ""
        sd = {}
        td = {}
        for c in t:
            td[c] = 1 + td.get(c,0)
        res = ""
        l=0
        r=0
        for i in range(len(s)):
            if s[i] in t:
                l=i
                r=i
                break
        freq = [0] * 128
        while r<len(s):
            freq[ord(s[r])]+=1
            if s[r] in t and sd.get(s[r],0) < td[s[r]]:
                sd[s[r]] = 1 + sd.get(s[r],0)
            # print(sd, l, r)
            if sd == td:
                # print(sd, l, r)
                if res == "" or len(res) > (r-l+1):
                    res = s[l:r+1]
                freq[ord(s[l])]-=1
                sd[s[l]] = min(sd[s[l]], freq[ord(s[l])])
                l+=1
            while l<r and ((s[l] not in t) or freq[ord(s[l])] > td[s[l]]):
                freq[ord(s[l])]-=1
                l+=1
            r+=1
        
        return res
        
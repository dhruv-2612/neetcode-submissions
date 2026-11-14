class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars1 = [0] * 26
        chars2 = [0] * 26
        if len(s1) > len(s2):
            return False

        for c in s1:
            chars1[ord(c)-ord('a')]+=1
        for i in range(len(s1)):
            chars2[ord(s2[i])-ord('a')]+=1
        if chars1 == chars2:
            return True
        r=len(s1)
        while r<len(s2):
            # print(chars2)
            chars2[ord(s2[r-len(s1)])-ord('a')]-=1
            chars2[ord(s2[r])-ord('a')]+=1
            if chars1 == chars2:
                return True
            r+=1
        return False
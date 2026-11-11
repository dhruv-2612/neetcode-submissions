from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        s_cnt = Counter(s)
        t_cnt = Counter(t)
        for c, cnt in s_cnt.items():
            if cnt != t_cnt[c]:
                return False
        return True
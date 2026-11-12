class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s="".join(char for char in s if char.isalnum())
        # print(s)
        st=0
        en=len(s)-1
        while(st<en and s[st]==s[en]):
            st+=1
            en-=1
        if st>=en:
            return True
        return False
        
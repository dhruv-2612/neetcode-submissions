class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for i in range(len(s)):
            if( s[i] in "[{("):
                arr.append(s[i])
            elif len(arr)>0 and (
                (arr[-1] == '[' and s[i] == ']') or
                (arr[-1] == '{' and s[i] == '}') or
                (arr[-1] == '(' and s[i] == ')')
            ):
                arr.pop()
            else:
                return False
        if len(arr)>0:
            return False
        return True
        
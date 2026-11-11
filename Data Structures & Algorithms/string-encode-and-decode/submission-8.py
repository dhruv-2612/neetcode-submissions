class Solution:

    def encode(self, strs: List[str]) -> str:
        return "@^!@".join(strs) + "@^!@" if strs!=[] else ""

    def decode(self, s: str) -> List[str]:
        return s[:-4].split("@^!@") if s!="" else []
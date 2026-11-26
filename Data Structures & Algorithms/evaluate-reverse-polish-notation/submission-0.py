class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stc = []
        for token in tokens:
            if token in "+-/*":
                num2 = int(stc.pop())
                num1 = int(stc.pop())
                if token == "+":
                    num1+=num2
                elif token == "-":
                    num1-=num2
                elif token == "/":
                    num1/=num2
                elif token == "*":
                    num1*=num2
                stc.append(int(num1))
            else:
                stc.append(token)
        return int(stc[0])

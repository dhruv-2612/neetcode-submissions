class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stc = [-1]
        for i in range(len(temperatures)):
            # print(stc)
            if stc[-1] == -1:
                stc.append(i)
            else:
                if(temperatures[stc[-1]] >= temperatures[i]):
                    stc.append(i)
                else:
                    while(stc[-1] != -1 and temperatures[stc[-1]] < temperatures[i]):
                        pop = stc.pop()
                        res[pop] = i - pop
                    stc.append(i)
        return res

        
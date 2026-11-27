from functools import cmp_to_key

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tpos = [[0,0] for i in range(len(position))]
        res = 0
        for i in range(len(position)):
            tpos[i][0], tpos[i][1] = (target-position[i])/speed[i], position[i]
        tpos.sort(key=cmp_to_key(self.posComp))
        # print(tpos)

        while tpos:
            temp = tpos.pop()
            while tpos and tpos[-1][0] <= temp[0]:
                tpos.pop()
            res+=1
        return res

    def posComp(self, a, b):
        if a[1]<b[1]:
            return -1
        elif a[1]>b[1]:
            return 1
        return 0

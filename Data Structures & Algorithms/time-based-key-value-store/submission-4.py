class TimeMap:

    def __init__(self):
        self.values = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        val = self.values.get(key,[])
        val.append([timestamp, value])
        self.values[key] = val

    def get(self, key: str, timestamp: int) -> str:
        vals = self.values.get(key, [])
        if vals == []:
            return ""
        st=0
        en=len(vals)-1
        m=(st+en)//2
        # print("get called", key, timestamp)
        # print(st, en)

        while st<=en:
            # print(st, m, en)
            if vals[m][0] == timestamp:
                return vals[m][1]
            elif vals[m][0] < timestamp:
                st=m+1
            else:
                en=m-1
            m=(st+en)//2
        if timestamp > vals[m][0]:
            return vals[m][1]
        return ""

        

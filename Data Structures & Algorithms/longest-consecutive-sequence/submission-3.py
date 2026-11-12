class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        master = set(nums)
        length=0
        while(len(master)>0):
            num=master.pop()
            temp_len=1
            sml=num-1
            lg=num+1
            while(sml in master):
                master.remove(sml)
                temp_len+=1
                sml-=1
            while(lg in master):
                master.remove(lg)
                temp_len+=1
                lg+=1
            if temp_len>length:
                length=temp_len
        
        return length
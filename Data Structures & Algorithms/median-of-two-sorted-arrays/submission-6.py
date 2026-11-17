class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if (len(nums1)>len(nums2)):
            t=nums1
            nums1=nums2
            nums2=t
        m=len(nums1)
        n=len(nums2)
        part=(m+n)//2
        l=0
        r=m-1
        i=(l+r)//2
        j=part-i-2

        # print(i, l, r)
        while True:
            print(i, j, l, r, part)

            # For nums1 (split at index i)
            max_left_x = nums1[i] if i >= 0 else float('-inf')
            min_right_x = nums1[i+1] if 0 <= (i+1) < m else float('inf')

            # For nums2 (split at index j)
            max_left_y = nums2[j] if j >= 0 else float('-inf')
            min_right_y = nums2[j+1] if 0 <= (j+1) < n else float('inf')
            if((max_left_x <= min_right_y) and (max_left_y <= min_right_x) ):
                if (m+n)%2:
                    return min(min_right_x, min_right_y)
                else:
                    return (max(max_left_x, max_left_y)+min( min_right_x, min_right_y))/2
            elif(max_left_x > min_right_y):
                r=i-1
            else:
                l=i+1
            i=(l+r)//2
            j=part-i-2
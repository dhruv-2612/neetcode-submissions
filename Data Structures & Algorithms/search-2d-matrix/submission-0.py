class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        st=0
        en=(m*n)-1
        mid=int((st+en)/2)
        while st<=en:
            if matrix[mid//n][mid%n] == target:
                return True
            elif matrix[mid//n][mid%n]>target:
                en=mid-1
            else:
                st=mid+1
            mid=int((st+en)/2)
        return False


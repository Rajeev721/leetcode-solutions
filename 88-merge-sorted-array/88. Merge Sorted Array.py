class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1,p2,p = m-1,n-1,m+n

        for ind in range(p-1,-1,-1):
            if p2 < 0:
                break
            if p1 >=0 and nums1[p1] > nums2[p2]:
                nums1[ind] = nums1[p1]
                p1 -= 1
            else:
                nums1[ind] = nums2[p2]
                p2 -= 1
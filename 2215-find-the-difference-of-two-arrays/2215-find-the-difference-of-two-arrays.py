class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        lista =[]
        listb =[]
        for i in nums1:
            if i not in nums2 and i not in lista:
                lista.append(i)
        for i in nums2:
            if i not in nums1 and i not in listb:
                listb.append(i)
        
        return [lista,listb]
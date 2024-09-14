class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic = set()
        l = []
        for i in nums:
            if i in dic:
                l.append(i)
            else:
                dic.add(i)

        return l

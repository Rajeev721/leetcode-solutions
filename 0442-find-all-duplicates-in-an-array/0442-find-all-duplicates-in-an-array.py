class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic = {}
        l = []
        for i in nums:
            if dic.get(i,None):
                dic[i] += 1
            else:
                dic[i] = 1
        for i,j in dic.items():
            if j > 1:
                l.append(i)

        return l

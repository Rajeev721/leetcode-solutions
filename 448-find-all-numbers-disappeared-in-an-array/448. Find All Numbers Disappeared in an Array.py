class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        set_len = set([i for i in range(1, len(nums)+1)])
        
        return set_len.difference(set_nums)

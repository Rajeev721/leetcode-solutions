class Solution:
    def rob(self, nums: List[int]) -> int:
        robb1 = robb2 = 0

        for i in nums:
            rob_val = max(robb1+i, robb2)
            robb1,robb2 = robb2, rob_val
        return rob_val

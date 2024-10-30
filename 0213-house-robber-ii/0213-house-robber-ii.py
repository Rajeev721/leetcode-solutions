class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1 = [0] * (len(nums) + 1)
        dp2 = [0] * (len(nums) + 1)
        if len(nums) == 1:
            return nums[0]

        def maxrob(dp,nums):
            dp[1] = nums[0]
            for i in range(2,len(nums) + 1):
                dp[i] = max(dp[i-1] , dp[i-2] + nums[i-1])
            return dp[len(nums)]
        max_rob = max(maxrob(dp1, nums[1:]), maxrob(dp2, nums[:-1]))
        return max_rob
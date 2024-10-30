class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        count = 0
        chars = set()
        for i in range(len(s)):
            while s[i] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[i])
            count = max(count, i-left+1)
        return count
        
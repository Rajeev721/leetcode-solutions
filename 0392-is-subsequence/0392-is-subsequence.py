class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left,right = len(s), len(t)

        left_ind = right_ind = 0

        while left_ind < left and right_ind < right:
            if s[left_ind] == t[right_ind]:
                left_ind += 1
            right_ind += 1
        return left_ind == left            
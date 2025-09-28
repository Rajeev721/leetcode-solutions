class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return
        else:
            if n > 1 and n %2 == 1:
                return False
        if n%2 == 0:
            return self.isPowerOfTwo(n//2)
        else:
            return True
        
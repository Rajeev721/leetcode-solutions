class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = ''
        if digits[0] == 0 and len(digits) > 1:
            pass
        else:
            for i in digits:
                sum = sum + str(i)
            return [int(x) for x in str(int(sum)+1)]
        
        
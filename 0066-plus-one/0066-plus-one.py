class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_str = ''.join([str(i) for i in digits])
        incr_digits_int = int(digits_str) + 1
        return [int(x) for x in str(incr_digits_int)]
            
        
        
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xored_ = x^y
        binary = bin(xored_)
        return str(binary).count('1')
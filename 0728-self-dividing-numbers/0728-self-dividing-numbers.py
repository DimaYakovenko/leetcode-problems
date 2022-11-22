class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [x for x in range(left, right + 1) if self.isSelfDividing(x)]
            
    
    def isSelfDividing(self, num: int) -> bool:
        copy = num
        while copy:
            rest = copy % 10
            if rest == 0 or num % rest != 0: 
                return False
            copy //= 10
        return True
        
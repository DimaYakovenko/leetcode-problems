class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num = 0
        count = 0
        for l in s:
            if l == 'R':
                count +=1
            else: 
                count -=1
            if count ==0:
                num += 1
        return num
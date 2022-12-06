class Solution:
    def isValid(self, s: str) -> bool:
        balance = []
        opening = set('({[')
        pairs = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in opening:
                balance.append(c)
            else:
                if len(balance) == 0:
                    return False
                if balance.pop() != pairs[c]:
                    return False
        return len(balance) == 0
            
        
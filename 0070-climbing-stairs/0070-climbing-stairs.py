class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.climbStairsRec(n, memo)
    
    def climbStairsRec(self, n: int, memo: dict) -> int:
        if n <= 1:
            return 1
        if n not in memo:
            memo[n] = self.climbStairsRec(n - 2, memo) + self.climbStairsRec(n - 1, memo)
        return memo[n]
        
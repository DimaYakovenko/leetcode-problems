class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        n = len(arr)
        
        for i in range(n):
            total = (n - i) * (i + 1)
            odd = total // 2
            if total % 2 != 0:
                odd += 1
            result +=  odd * arr[i]
        return result
        
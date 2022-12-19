class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        result = sum(arr)
        if len(arr) % 2 != 0:
            result *= 2
        sub_size = 3
        while sub_size < len(arr):
            i = 0
            while i < len(arr) - sub_size + 1:
                result += sum(arr[i:i + sub_size])
                i += 1
            sub_size += 2

        return result
        
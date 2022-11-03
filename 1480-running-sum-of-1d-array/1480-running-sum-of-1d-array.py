class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        subSum = 0
        for i in range(0, len(nums)):
            subSum += nums[i]
            res.append(subSum)
        return res
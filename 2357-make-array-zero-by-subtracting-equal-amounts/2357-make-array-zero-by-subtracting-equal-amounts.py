class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        ops = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            subtr = nums[i]
            for j in range(i, len(nums)):
                nums[j] = nums[j] - subtr
            ops += 1
        return ops
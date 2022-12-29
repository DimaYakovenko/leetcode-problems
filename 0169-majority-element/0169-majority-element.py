class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n_to_freq = {}
        for n in nums:
            if n not in n_to_freq:
                n_to_freq[n] = 1
            else:
                n_to_freq[n] += 1
            if n_to_freq[n] > len(nums)//2:
                return n
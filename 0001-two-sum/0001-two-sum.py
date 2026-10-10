class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        d = {}

        for i in range(0,n):
            remaining = target-nums[i]
            if remaining in d:
                return [d[remaining],i]
            d[nums[i]] = i
        
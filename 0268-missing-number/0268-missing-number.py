class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        c=sum(nums)
        b = len(nums)
        a = b*(b+1)/2
        return int(a-c)
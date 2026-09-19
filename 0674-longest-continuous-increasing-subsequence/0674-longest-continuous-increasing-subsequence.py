class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 1
        j = 1

        for k in range(1,len(nums)):
            if nums[k] > nums[k-1]:
                j+=1
            else:
                i = max(i,j)
                j = 1
        return max(i,j)

        
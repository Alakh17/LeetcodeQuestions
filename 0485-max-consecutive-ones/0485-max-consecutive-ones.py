class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        c = 0
        max_c = 0

        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
            else:
                max_c = max(max_c,c)
                c=0
        return max(max_c,c)

        
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        j = 0

        for k in nums:
            if k ==1:
                i+=1
            else:
                j = max(j,i)
                i=0
        return max(j,i)

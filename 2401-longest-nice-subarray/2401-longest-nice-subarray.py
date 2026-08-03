class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        i = 0
        j = 0
        maxi = 0
        bits = 0

        while j < len(nums):
            if bits & nums[j]==0:
                bits |= nums[j]
                maxi = max(maxi,j-i+1)
                j+=1
            else:
                bits^=nums[i]
                i+=1
                
        return(maxi) 



        
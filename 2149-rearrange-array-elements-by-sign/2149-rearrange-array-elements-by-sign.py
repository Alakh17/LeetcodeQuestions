class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        positive = 0
        negative = 1

        for i in range(len(nums)):
            if nums[i]>= 0:
                res[positive] = nums[i]
                positive+=2
            else:
                res[negative] = nums[i]
                negative +=2
        return res

        
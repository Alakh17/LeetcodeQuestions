class Solution:

    def fun(self,ind,nums,subset,result):
        if ind >= len(nums):
            result.append(subset.copy())
            return 
        subset.append(nums[ind])
        self.fun(ind+1,nums,subset,result)
        subset.pop()
        self.fun(ind+1,nums,subset,result)
        
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        self.fun(0,nums,[],result)
        return result
        

        

        


        
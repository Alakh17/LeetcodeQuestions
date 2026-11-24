class Solution:
    def solve(self,ind,total,subset,nums,result):
        if total == 0:
            result.append(subset.copy())
            return
        if total < 0:
            return
        for i in range(ind,len(nums)):
            if i > ind and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            Sum = total-nums[i]
            self.solve(i+1,Sum,subset,nums,result)
            subset.pop()

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        self.solve(0,target,[],candidates,result)
        return result
        
        
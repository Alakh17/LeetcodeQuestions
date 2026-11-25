class Solution:
    def solve(self,ind,total,subset,result,k,n):
        if total == n and len(subset)==k:
            result.append(subset.copy())
            return 
        if total > n or len(subset)>k:
            return
        for i in range(ind,10):
            Sum = total+i
            subset.append(i)
            self.solve(i+1,Sum,subset,result,k,n)
            subset.pop()
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []
        self.solve(1,0,[],result,k,n)
        return result
        
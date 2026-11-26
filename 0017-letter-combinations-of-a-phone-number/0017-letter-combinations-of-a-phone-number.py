class Solution:
    char_map = {
        "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"     
    }
    def solve(self,ind,subset,result,digits):
        if ind >= len(digits):
            result.append("".join(subset))
            return
        for ch in self.char_map[digits[ind]]:
            subset.append(ch)
            self.solve(ind+1,subset,result,digits)
            subset.pop()
    def letterCombinations(self, digits: str) -> list[str]:
        result = []
        self.solve(0,[],result,digits)
        return result
        
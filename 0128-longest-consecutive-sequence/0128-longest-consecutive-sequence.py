class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set(nums)
        
        longest = 0

        for i in a:
            if i-1 not in a:
                x = i
                c=1
                while x+1 in a:
                    c+=1
                    x+=1
                longest = max(longest,c)
        return longest



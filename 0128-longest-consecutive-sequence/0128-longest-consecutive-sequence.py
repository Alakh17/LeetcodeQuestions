class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        a = set()
        for i in range(len(nums)):
            a.add(nums[i])
        longest = 0

        for i in a:
            if i-1 not in a:
                x = i
                count=1

                while x+1 in a:
                    count+=1
                    x+=1
                longest = max(longest,count)
        return longest

        
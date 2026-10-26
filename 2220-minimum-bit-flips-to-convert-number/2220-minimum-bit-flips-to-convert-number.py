class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start ^ goal
        c = 0
        for i in range(32):
            if ans &(1<<i)!=0:
                c+=1
        return c
        
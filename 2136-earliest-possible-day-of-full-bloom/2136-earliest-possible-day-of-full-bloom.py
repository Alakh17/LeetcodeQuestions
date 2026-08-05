class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        a = sorted(zip(growTime,plantTime), reverse = True)

        ans = 0
        curr = 0

        for i,j in a:
            curr+= j
            ans = max(ans, curr+i)
        return ans
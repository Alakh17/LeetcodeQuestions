class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minimum = min(nums)
        moves = 0

        for i in nums:
            if i != minimum:
                moves += i-minimum
        return moves


        
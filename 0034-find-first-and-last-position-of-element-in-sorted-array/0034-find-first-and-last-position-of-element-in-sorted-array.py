class Solution:
    def lower_bound(self,nums,target):
        n = len(nums)
        lb= n
        low = 0 
        high = n-1

        while low<=high:
            mid = (low+high)//2
            if nums[mid]>=target:
                lb = mid
                high = mid-1
            else:
                low = mid+1
        return lb

    def upper_bound(self,nums,target):
        n = len(nums)
        ub = n
        low = 0
        high = n-1

        while low<=high:
            mid = (low+high)//2
            if nums[mid] > target:
                ub = mid
                high = mid-1
            else:
                low = mid+1
        return ub


    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lb = self.lower_bound(nums,target)
        if lb == len(nums) or nums[lb]!= target:
            return [-1,-1]
        ub = self.upper_bound(nums,target)

        return [lb, ub-1]
        
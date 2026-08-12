class Solution:
    def merge(self,left,right):
        arr=[]
        i,j = 0,0
        n = len(left)
        m = len(right)

        while i < n and j < m:
            if left[i]<=right[j]:
                arr.append(left[i])
                i+=1
            else:
                arr.append(right[j])
                j+=1
        if i<n:
            while i<n:
                arr.append(left[i])
                i+=1
        if j<m:
            while j<m:
                arr.append(right[j])
                j+=1
        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        left_arr = self.sortArray(left)
        right_arr = self.sortArray(right)
        return self.merge(left_arr,right_arr)
        
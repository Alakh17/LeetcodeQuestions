class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]

        for i in arr:
            prefix.append(prefix[-1] ^ i)

        ans = []
        for l ,r in queries:
            ans.append(prefix[r+1] ^ prefix[l])
        return ans 
        

        # ans = []
        # for l,r in queries:
        #     product = 0
        #     for i in range(l,r+1):
        #         product ^= arr[i]
        #     ans.append(product)
        # return ans
             

        
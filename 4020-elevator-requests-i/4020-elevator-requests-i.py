class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:

        curr = requests[0]
        

        for i in range(1,len(requests)):
            curr+= abs(requests[i]-requests[i-1])
    
        return curr
            
        
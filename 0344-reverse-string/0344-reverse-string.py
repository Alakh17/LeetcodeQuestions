class Solution:
    def rev(self, l ,r,s):
        if l>=r:
            return 
        s[l],s[r] = s[r], s[l]
        self.rev(l+1,r-1,s)
    def reverseString(self, s: List[str]) -> None:
        self.rev(0,len(s)-1,s)
        return s
        
        """
        Do not return anything, modify s in-place instead.
        """
        
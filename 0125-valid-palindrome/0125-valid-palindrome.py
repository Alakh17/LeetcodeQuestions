class Solution:
    def fun(self,s,l,r):
        if l>=r:
            return True
        if s[l]!=s[r]:
            return False
        return self.fun(s,l+1,r-1)

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(i for i in s if i.isalnum())
        return self.fun(s,0,len(s)-1)

        
        
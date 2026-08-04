class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        result = 0

        while n>0:
            j = n%10
            result = (result*10)+j
            n = n//10
        return x == result
        
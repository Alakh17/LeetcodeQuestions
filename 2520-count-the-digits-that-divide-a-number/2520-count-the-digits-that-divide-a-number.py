class Solution:
    def countDigits(self, num: int) -> int:
        n = num
        c=0
        while n > 0:
            a = n%10
            if num % a == 0:
                c+=1
            n = n//10
        return c

        
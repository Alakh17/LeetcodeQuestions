class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        n = len(a)

        for start in range(0,n,2*k):
            i = start
            j = min(start + k-1, n-1)
            while i <j:
                a[i],a[j] = a[j],a[i]
                i+=1
                j-=1
        return "".join(a)

        
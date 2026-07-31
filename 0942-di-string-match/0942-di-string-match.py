class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l = 0 
        h = len(s)
        res= []

        for i in s:
            if i == "I":
                res.append(l)
                l+=1
            else:
                res.append(h)
                h-=1
        return res +[l]
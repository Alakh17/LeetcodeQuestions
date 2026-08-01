class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        a = set()
        res = set()

        for i in range(len(s)-9):
            cur = s[i:i+10]
            if cur in a:
                res.add(cur)
            a.add(cur)
        return list(res)
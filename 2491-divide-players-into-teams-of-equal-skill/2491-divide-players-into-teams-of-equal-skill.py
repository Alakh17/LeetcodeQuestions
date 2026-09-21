class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i , j = 0, len(skill)-1
        arr = []
        s = skill[0] + skill[-1]

        while i<j:
            if skill[i] + skill[j] != s:
                return -1
            else:
                arr.append((skill[i],skill[j]))
            i+=1
            j-=1
        total = sum(i[0]*i[1] for i in arr)
        return total

        
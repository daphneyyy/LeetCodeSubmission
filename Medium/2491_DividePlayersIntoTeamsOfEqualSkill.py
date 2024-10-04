# 2491. Divide Players Into Teams of Equal Skill

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        k = n // 2
        sum_skill = sum(skill)
        if sum_skill % k != 0:
            return -1

        ttl = sum_skill // k
        lst = sorted(skill)
        res = 0
        for i in range(k):
            if lst[i] + lst[-i-1] != ttl:
                return -1
            res += lst[i] * lst[-i-1]
        return res

        

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill_per_team=sum(skill)*2//len(skill)
        skill=sorted(skill)
        r=len(skill)-1
        chem=0
        for i in range(len(skill)//2):
            if skill[i]+skill[r]==skill_per_team:
                chem+=skill[i]*skill[r]
                r-=1
            else:
                return -1
        return chem

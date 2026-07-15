from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1=Counter(s1)
        width=len(s1)
        c2=Counter(s2[:width])
        if c1==c2:
            return True
        l,r=0,width
        for i in range(width,len(s2)):
            c2[s2[i]]+=1
            c2[s2[i-width]]-=1
            if c1==c2:
                return True
        return False

        
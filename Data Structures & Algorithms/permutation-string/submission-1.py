from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cc=Counter(s1)
        s3="".join(i if i in set(s1) else '_' for i in s2)
        s4=[j for j in s3.split("_") if j != '']
        n=len(s1)
        for k in s4:
            if len(k)==len(s1) and Counter(k)==cc:
                return True
            l,m=0,n
            while m<=len(k):
                if Counter(k[l:m])==cc:
                    return True
                l+=1
                m+=1
        
        return False
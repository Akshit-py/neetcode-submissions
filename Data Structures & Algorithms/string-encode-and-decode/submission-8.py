import re
class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        for i in strs:
            s+=str(len(i))
            s+='!;!'
            s+=i
            s+='!mm!'
        return s

    def decode(self, s: str) -> List[str]:
        il=s.split("!mm!")
        fl=[]
        for i in il[:-1]:
            fl.append(i.split('!;!')[1])
        
        return fl

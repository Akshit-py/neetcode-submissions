class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictList={}
        nstr=[]
        fstr=[]
        if len(strs)==0:
            return [""]
        for i in strs:
            nstr.append(''.join(sorted(i)))
        for x in sorted(nstr):
            dictList[x]=[i for i, val in enumerate(nstr) if val == x]
        for i in dictList.values():
            fstr.append([strs[j] for j in i])
        return fstr
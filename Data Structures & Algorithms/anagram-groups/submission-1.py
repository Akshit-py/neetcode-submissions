class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictList={}
        
        for t in strs:
            t_sorted="".join(sorted(t))
            if t_sorted in dictList:
                dictList[t_sorted].append(t)
            else:
                dictList[t_sorted]=[t]
        fList=[]
        for keys in dictList:
            fList.append(dictList[keys])
        return fList
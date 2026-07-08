import itertools
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        fl=[]
        for i in range(0,len(numbers)):
            comp=target-numbers[i]
            if comp in numbers[i+1:]:
                fl.append([numbers[i],comp])
        return fl
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        finalList=[]
        for i in range(0,len(nums)):
            comp=0-nums[i]
            imList=self.twoSum(nums[i+1:],comp)
            if len(imList)>0:
                for j in imList:
                    finalList.append(sorted([nums[i],j[0],j[1]]))
        finalList.sort()
        j=list(k for k,_ in itertools.groupby(finalList))
        return j


        
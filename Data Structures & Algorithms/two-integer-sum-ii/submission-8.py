class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0,len(numbers)):
            comp=target-numbers[i]
            if comp in numbers[i+1:]:
                return[i+1,numbers.index(comp,i+1)+1]

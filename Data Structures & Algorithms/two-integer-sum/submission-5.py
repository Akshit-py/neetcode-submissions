class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            comp=target-nums[i]
            if comp in nums[i+1:]:
                return [i,nums.index(comp,i+1)]
            else:
                pass
        
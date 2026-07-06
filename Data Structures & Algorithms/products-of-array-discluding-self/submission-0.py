import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount=nums.count(0)
        if zeroCount>1:
            return [0]*len(nums)
        elif zeroCount==1:
            zeroIndex=nums.index(0)
            numsProd=math.prod(nums[:zeroIndex] + nums[zeroIndex + 1:])
            fl=[0]*len(nums)
            fl[zeroIndex]=numsProd
            return fl
        else:
            numsProd=math.prod(nums)
            fl=[int(numsProd/i) for i in nums]
            return fl
        

        
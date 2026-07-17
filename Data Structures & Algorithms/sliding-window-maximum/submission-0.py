class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k>len(nums):
            return max(nums)
        res=[]
        l=0
        while k<=len(nums):
            res.append(max(nums[l:k]))
            l+=1
            k+=1
        
        return res

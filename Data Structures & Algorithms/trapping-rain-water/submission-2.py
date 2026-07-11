class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<=2:
            return 0
        l=0
        r=len(height)-1
        maxl=height[l]
        maxr=height[r]
        vol=0
        while l<r:
            if maxl<=maxr:
                l +=1
                maxl=max(maxl,height[l])
                vol += maxl-height[l]
            else:
                r -=1
                maxr=max(maxr,height[r])
                vol +=  maxr-height[r]
        
        return vol


        
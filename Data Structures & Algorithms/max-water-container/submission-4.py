class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=len(heights)-1
        i=0
        water=0
        while l>i:
            w=(l-i)*min(heights[i],heights[l])
            water=max(w,water)
            if heights[i]<heights[l]:
                i=i+1
            else:
                l=l-1
        return water



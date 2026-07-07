class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        fl=sorted(nums)
        longest=0

        for i in fl:
            if (i-1) not in fl:
                current = i
                streak = 1

                while (current+1) in fl:
                    current +=1
                    streak  +=1
                
                longest=max(longest,streak)
        
        return longest
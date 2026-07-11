class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range (0,len(prices)):
            b=prices[i]
            #print("buy: ",b)
            if len(prices[i+1:])>0:
                s=max(prices[i+1:])
                if s-b>profit:
                    profit=s-b
            #print(profit)
        
        return profit
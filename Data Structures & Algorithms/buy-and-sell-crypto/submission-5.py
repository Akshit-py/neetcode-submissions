class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(prices==sorted(prices,reverse=True)):
            return 0
        profit=0
        while len(prices)>0:
            b=min(prices)
            ib=prices.index(b)
            if ib==len(prices)-1:
                prices=prices[:-1]
                continue
            s=max(prices[ib:])
            if s-b>profit:
                profit=s-b
            prices=prices[:ib]+prices[ib+1:]
        return profit

# Best time to buy and sell Stock
class Besttime_stock():
    def maxprofit(self, prices: list):
        result = []
        for i in prices:
            buy_index = prices.index(i)
            for j in prices:
                if prices.index(j) <= buy_index:
                    pass
                else:
                    if prices.index[j]+1 <= len(prices) -1:
                        a = i - prices[prices.index(j)+1]
                        result.append(a)

        return result

prices = [1,5,2,3,4]
print(Besttime_stock().maxprofit(prices))
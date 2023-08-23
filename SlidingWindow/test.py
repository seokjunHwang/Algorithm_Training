# prices = [1,5,2,3,4]
# print(prices[prices.index(5)+1])
# print(len(prices)-1)

my_list = [10, 5,5 ,10,20,20, 15, 30]
sorted_list = sorted(my_list, reverse=True)
print(sorted_list)

class BesttimeStock():
    def maxprices(self, prices):
        result = []

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[i] < prices[j]:
                    profit = prices[j] - prices[i]
                    result.append(profit)

        return max(result) if result else 0

my_list = [10, 5, 5, 10, 20, 20, 15, 30]
print(BesttimeStock().maxprices(my_list))
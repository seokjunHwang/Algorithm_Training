# 지피티3.5 도움
# for i in prices로 처음에 인자를 직접적으로 가져오려고했으나,
# 인자의 인덱스의 범위를 for i in range()로 정하여 구현하면 더 쉽다는걸 깨달음.
# + 날짜까지 알 수 있는방법도 구현해보기.

class BesttimeStock():
    def maxprices(self, prices):
        sorted_prices = sorted(prices, reverse = True)
        result = []

        if prices == sorted_prices:
            return 0
        
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                a = prices[j] - prices[i]
                result.append(a)
        return max(result)

    # 매수,매도날짜까지 아는 코드
    def find_date(self, prices):
        max_price = 0
        buy_date = 0
        sell_date = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                price = prices[j] - prices[i]
                if price > max_price:
                    max_price = price
                    buy_date = i
                    sell_date = j
        return max_price, buy_date, sell_date

my_list = [10, 5,5 ,3,31]
print(BesttimeStock().maxprices(my_list))
print(BesttimeStock().find_date(my_list))
# two pointer 사용

class Solution():
    def maxprofit(self, prices):
        l, r = 0, 1 # left = buy, right = sell
        max_price = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                price = prices[r] - prices[l]
                max_price = max(max_price, price) # max of ( max_price or price ) 
            else:
                l = r # l +=1가 불필요한 움직임이다. r위치의 값이 buy보다 더 작으면 처음시작점보다 더 작은것이 될테니
                # 그냥 buy를 r위치로 바로 옮기는것이 좋다. 
            r += 1
        return max_price # if r is over the prices list's length, return max_price 
    
prices = [7,4,3,2,1] # if there's no profit in any way, max_price remains at 0
print(Solution().maxprofit(prices))

        


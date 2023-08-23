import array
import pandas as pd

class Solution:
    def containsDuplicate(self, numbers):
        num_list = []
        
        for i in numbers:
            num_list.append(i)

        num_set = list(set(num_list)) # set으로 중복을 없애고 다시 list로 변환
        
        print(num_list)
        print(num_set)

        if num_list == num_set: # 중복있는것과 없는것을 비교
            print("false")
        else:
            print("ture")

        return

numbers = [1,2,3,4,1,2]
Solution().containsDuplicate(numbers)

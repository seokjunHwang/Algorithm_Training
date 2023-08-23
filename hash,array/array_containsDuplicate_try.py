import array
import pandas as pd

class Solution(object):


    def containsDuplicate(self, numbers):
        num_list = []

        for i in self.numbers:
            i = int()
            num_list.append(i)
            
            if num_list == set():
                print(f"{num_list}\nfalse")
                
            else:
                print(f"{num_list}\ntrue")
        """
        :type nums: List[int]
        :rtype: bool
        """
numbers = [1,2,3,1]
Solution.containsDuplicate(numbers)
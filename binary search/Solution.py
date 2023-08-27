# Given an array of integers nums which is sorted in ascending order, and an integer target, 
# = 오름차순 정렬된 배열이 주어지면..
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.
from typing import List

class BinarySearch:
    def search(self, nums: List[int], target:int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:  # Repeat until l is less than or equal to r
            m = l + ((r - l) // 2) # middle index
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m  # return index of the target
        return -1 # if target is not exist in the nums, return -1
    
num_list = [1,5,6,8,9,10,11,12]
target_value = 11
print(BinarySearch().search(num_list,target_value))

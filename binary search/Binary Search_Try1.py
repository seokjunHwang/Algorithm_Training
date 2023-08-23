import math

class BinarySearch(object):
    def search(self, nums : list, target : int) -> int:
        if len(nums) == len(set(nums)):
            if target in nums:
                nums.sort()
                
                while True:
                    # Find middle value
                    if len(nums) % 2 == 1:
                        middle_index = int(math.floor(len(nums))/2)
                    else:
                        middle_index = int(len(nums)/2 - 1 )
                    middle_value = nums[middle_index]
                    print(middle_index)

                    # Mach middle : target
                    if middle_value == target:
                        return middle_value
                        break
                    elif middle_value < target:
                        nums = nums[middle_index+1:]
                        print(nums)
                    else:
                        nums = nums[:middle_index+1] # 슬라이싱의 끝은 그 직전까지라서 +1을 해줘야함.
                        print(nums)
            else:
                return -1

        else:
            print("There are duplicate values in the s list.")


a = [7,3,1,4,5,2]
target = 7

print(BinarySearch().search(a,target))








# 문제)
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

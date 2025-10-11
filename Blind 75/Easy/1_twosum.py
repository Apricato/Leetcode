#1. TWO SUM

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

nums_input = []

class Solution(object):
    def twoSum(self, nums, target):
       for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target:
                    return [x, y]
#Input 
while len(nums_input)<2 and len(nums_input)> 10**4:
    raw=input("Enter the values withing your array, use spaces in between each value:")
    nums_input = list(map(int,raw.split()))
    if len(nums_input)<2:
        print("Oops! You need to add at least 2 number")
        print("")

        



target= int(input("Enter your target value:"))
#Output
solution = Solution()
result= solution.twoSum(nums_input,target)
print(f"Indexes that add up to {target} : {result}")



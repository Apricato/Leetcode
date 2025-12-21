'''Given an integer array nums , return true if any value appears more than once in the array otherwise return false
    Example 1 :
        Input: nums = [ 1,2,3,4]
        output:true

    Example 2:
        Input: nums = [1, 2, 3, 4]
        Output: false

'''

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


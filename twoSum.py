# Problem - Two Sum 
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, number in enumerate(nums):
            complement = target - number
            if hm.get(complement) != None:
                return [i, hm.get(complement)]
            hm[number] = i
        return []
sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
            

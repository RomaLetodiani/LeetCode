class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {} # O(1)
        for index, num in enumerate(nums): # O(N)
            needed = target - num # O(1)
            if needed in found: # O(1)
                return [index, found[needed]] # O(1)
            found[num] = index # O(1)
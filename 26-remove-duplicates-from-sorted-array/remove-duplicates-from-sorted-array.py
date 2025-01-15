class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1

        for a in range(1, len(nums)):
            if nums[a] != nums[k - 1]:
                nums[k] = nums[a]
                k += 1
        
        return k
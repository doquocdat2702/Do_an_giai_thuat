class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 2  # first two elements are always valid

        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:  # allow at most 2 of each
                nums[k] = nums[i]
                k += 1

        return k
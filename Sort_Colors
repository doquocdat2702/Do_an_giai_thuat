class Solution:
    def sortColors(self, nums):

        left = 0
        current = 0
        right = len(nums) - 1

        while current <= right:

            # Nếu là 0
            if nums[current] == 0:

                nums[left], nums[current] = nums[current], nums[left]

                left += 1
                current += 1

            # Nếu là 2
            elif nums[current] == 2:

                nums[current], nums[right] = nums[right], nums[current]

                right -= 1

            # Nếu là 1
            else:
                current += 1
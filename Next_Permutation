class Solution:
    def nextPermutation(self, nums):

        n = len(nums)

        # 1. Tìm điểm giảm đầu tiên từ phải sang trái
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2. Nếu tìm thấy
        if i >= 0:

            # Tìm số lớn hơn nums[i] từ bên phải
            j = n - 1

            while nums[j] <= nums[i]:
                j -= 1

            # Hoán đổi
            nums[i], nums[j] = nums[j], nums[i]

        # 3. Đảo ngược phần phía sau
        left = i + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
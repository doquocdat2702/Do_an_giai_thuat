class Solution:
    def jump(self, nums):

        jumps = 0
        current_end = 0
        farthest = 0

        # Không cần duyệt phần tử cuối
        for i in range(len(nums) - 1):

            # Xa nhất có thể tới
            farthest = max(farthest, i + nums[i])

            # Hết phạm vi của jump hiện tại
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps
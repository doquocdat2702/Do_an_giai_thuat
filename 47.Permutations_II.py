class Solution:
    def permuteUnique(self, nums):

        nums.sort()

        result = []

        def backtrack(path, used):

            # Nếu đủ phần tử
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):

                # Nếu đã dùng
                if used[i]:
                    continue

                # Bỏ duplicate
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                # Chọn phần tử
                used[i] = True
                path.append(nums[i])

                backtrack(path, used)

                # Backtrack
                path.pop()
                used[i] = False

        backtrack([], [False] * len(nums))

        return result
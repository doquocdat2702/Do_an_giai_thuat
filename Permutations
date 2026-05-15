class Solution:
    def permute(self, nums):

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

                # Chọn phần tử
                path.append(nums[i])
                used[i] = True

                # Đệ quy
                backtrack(path, used)

                # Backtrack
                path.pop()
                used[i] = False

        backtrack([], [False] * len(nums))

        return result
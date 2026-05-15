class Solution:
    def combinationSum(self, candidates, target):

        result = []

        def backtrack(start, path, total):

            # Nếu đạt target
            if total == target:
                result.append(path[:])
                return

            # Nếu vượt target
            if total > target:
                return

            for i in range(start, len(candidates)):

                # Chọn phần tử hiện tại
                path.append(candidates[i])

                # Có thể dùng lại nên truyền i
                backtrack(i, path, total + candidates[i])

                # Backtrack
                path.pop()

        backtrack(0, [], 0)

        return result
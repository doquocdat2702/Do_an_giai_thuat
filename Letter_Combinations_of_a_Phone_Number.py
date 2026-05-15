class Solution:
    def letterCombinations(self, digits):

        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(index, path):

            # Nếu tạo đủ ký tự
            if index == len(digits):
                result.append(path)
                return

            # Lấy các chữ cái của số hiện tại
            letters = phone[digits[index]]

            for char in letters:
                backtrack(index + 1, path + char)

        backtrack(0, "")

        return result
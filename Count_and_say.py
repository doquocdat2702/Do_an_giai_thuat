class Solution:
    def countAndSay(self, n):

        result = "1"

        for _ in range(n - 1):

            current = ""
            count = 1

            for i in range(1, len(result)):

                # Nếu ký tự giống nhau
                if result[i] == result[i - 1]:
                    count += 1
                else:
                    # Thêm count + ký tự
                    current += str(count) + result[i - 1]
                    count = 1

            # Thêm nhóm cuối cùng
            current += str(count) + result[-1]

            result = current

        return result
class Solution:
    def multiply(self, num1, num2):

        # Nếu có số 0
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        result = [0] * (m + n)

        # Nhân từ phải sang trái
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                mul = int(num1[i]) * int(num2[j])

                p1 = i + j
                p2 = i + j + 1

                total = mul + result[p2]

                result[p2] = total % 10
                result[p1] += total // 10

        # Chuyển sang string
        answer = ""

        for num in result:
            if not (len(answer) == 0 and num == 0):
                answer += str(num)

        return answer
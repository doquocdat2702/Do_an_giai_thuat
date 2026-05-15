class Solution:
    def myAtoi(self, s):

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        i = 0
        n = len(s)

        # Bỏ khoảng trắng đầu
        while i < n and s[i] == ' ':
            i += 1

        # Xác định dấu
        sign = 1
        if i < n and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1

        # Đọc số
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # Kiểm tra overflow
            if result > (INT_MAX - digit) // 10:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result
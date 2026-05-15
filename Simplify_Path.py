class Solution:
    def simplifyPath(self, path):

        stack = []

        # Tách theo "/"
        parts = path.split("/")

        for part in parts:

            # Bỏ rỗng và "."
            if part == "" or part == ".":
                continue

            # Quay lại thư mục cha
            elif part == "..":
                if stack:
                    stack.pop()

            # Thư mục hợp lệ
            else:
                stack.append(part)

        return "/" + "/".join(stack)
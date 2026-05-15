class Solution:
    def minDepth(self, root):
        if not root:
            return 0

        # Nếu 1 trong 2 nhánh bị null
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left),
                       self.minDepth(root.right))

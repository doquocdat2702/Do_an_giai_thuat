class Solution:
    def rotateRight(self, head, k):

        if not head or not head.next or k == 0:
            return head

        # Tính độ dài list
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Nối thành vòng tròn
        tail.next = head

        # K có thể lớn hơn length
        k = k % length

        # Tìm vị trí tail mới
        steps = length - k - 1

        new_tail = head

        for _ in range(steps):
            new_tail = new_tail.next

        # Head mới
        new_head = new_tail.next

        # Cắt vòng tròn
        new_tail.next = None

        return new_head
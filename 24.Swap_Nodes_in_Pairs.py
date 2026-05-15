class Solution:
    def swapPairs(self, head):

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while prev.next and prev.next.next:

            # Hai node cần đổi
            first = prev.next
            second = prev.next.next

            # Swap
            first.next = second.next
            second.next = first
            prev.next = second

            # Di chuyển prev
            prev = first

        return dummy.next
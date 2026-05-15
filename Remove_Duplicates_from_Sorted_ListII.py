class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pred = dummy  
        while pred.next and pred.next.next:
            if pred.next.val == pred.next.next.val:
                dup_val = pred.next.val

               
                while pred.next and pred.next.val == dup_val:
                    pred.next = pred.next.next
            else:
                pred = pred.next  
        return dummy.next
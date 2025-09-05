class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                # skip the duplicate
                current.next = current.next.next
            else:
                current = current.next
        return head

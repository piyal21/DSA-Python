# Find the cycle in linked list : 
# Tortoise and hare method
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow : 
                return True 
        return False
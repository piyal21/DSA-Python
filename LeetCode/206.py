class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        temp = head

        while temp is not None:
            front_node = temp.next
            temp.next = prev_node 
            prev_node = temp
            temp = front_node
        return prev_node
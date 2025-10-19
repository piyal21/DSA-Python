

# Function to identify the length of a cycle in a linked list
# T(C)=O(N) 
# S(C)=O(1)

def find_cycle_length(head):
    slow , fast = head,head
    
    while fast is not None and fast.next is not None:
        slow = slow.next 
        fast = fast.next 
        
        if slow == fast: # Loop detected
            slow = slow.next 
            count =1 
            while slow !=fast:
                slow = slow.next 
                count +=1 
            return count
    return 0
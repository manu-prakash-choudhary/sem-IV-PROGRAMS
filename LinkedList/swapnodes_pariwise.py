class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap_pairs(head):
    # If the list has less than two nodes or is empty, no swapping needed
    if not head or not head.next:
        return head
    
    # Dummy node to simplify the code
    dummy = ListNode(0)
    dummy.next = head
    
    # Pointer to keep track of the current node
    current = dummy
    
    while current.next and current.next.next:
        # Nodes to be swapped
        first_node = current.next
        second_node = current.next.next
        
        # Swapping
        first_node.next = second_node.next
        second_node.next = first_node
        current.next = second_node
        
        # Move current pointer two steps forward
        current = current.next.next
    
    return dummy.next

# Function to print the linked list
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

print("Original linked list:")
print_list(head)

# Swap nodes pairwise
head = swap_pairs(head)

print("Linked list after pairwise swapping:")
print_list(head)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

# Function to create a linked list with predefined values
def create_linked_list(values):
    head = None
    current = None

    for val in values:
        new_node = ListNode(val)
        if not head:
            head = new_node
            current = new_node
        else:
            current.next = new_node
            current = new_node

    return head

# Function to print values from the middle node to the end
def print_values_from_middle(head):
    current = head

    while current:
        print(current.val)
        current = current.next

# Main function
if __name__ == "__main__":
    # Predefined values for the linked list: 1 -> 2 -> 3 -> 4 -> 5
    values = [1, 2, 3, 4, 5]

    # Create the linked list
    head = create_linked_list(values)

    solution = Solution()

    # Find the middle node
    middle = solution.middleNode(head)

    # Print values from the middle node to the end
    print("Values from the middle node to the end:")
    print_values_from_middle(middle)

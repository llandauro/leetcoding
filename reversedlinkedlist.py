# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        temp = None
        node = None
        

        while head != None: 
            # first let's make node 1 point to None:
            # first we don't want to lose head.next (aka 2):
            temp = head.next # now dummy1 has 2
            head.next = node # which is null right now so 1 points to null
            node = head
            head = temp

        return node 
    
# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list to a list of values for easy verification
def linked_list_to_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values

# Test the reverseList function
if __name__ == "__main__":
    # Create the linked list [1, 2, 3, 4, 5]
    input_list = [1, 2, 3, 4, 5]
    head = create_linked_list(input_list)
    
    # Reverse the linked list
    solution = Solution()
    reversed_head = solution.reverseList(head)
    
    # Convert the reversed linked list back to a Python list and print it
    reversed_list = linked_list_to_list(reversed_head)
    print("Reversed Linked List:", reversed_list)

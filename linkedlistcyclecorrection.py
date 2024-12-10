#Floyd's Tortoise and Hare algorithm: 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def create_linked_list_with_cycle(values, pos):
    if not values:
        return None  # No nodes to create
    
    # Create the head node
    head = ListNode(values[0])
    current = head
    
    # Dictionary to store the nodes by their index
    nodes = {0: head}
    
    # Create the rest of the nodes
    for i in range(1, len(values)):
        node = ListNode(values[i])
        current.next = node
        current = node
        nodes[i] = node
    
    # Create the cycle by linking the tail to the node at position `pos`
    if pos != -1 and pos < len(values):
        current.next = nodes[pos]
    
    return head

values = [3, 2, 0, -4]
pos = 1
test_head = create_linked_list_with_cycle(values, pos)


def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
        
    tortoise = head 
    rabbit = head

    while rabbit and rabbit.next: 
            tortoise = tortoise.next
            rabbit = rabbit.next.next
            if tortoise == rabbit:
                return True

    return False

print(hasCycle(test_head))

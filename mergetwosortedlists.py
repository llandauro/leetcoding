# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode(0, None)
        index = 0
        final_list = ListNode(0, None)

        if list1 == None and list2 == None:
            return None

        while list1 != None and list2 != None:
            if list1.val > list2.val: 
                final_list.next = ListNode(list2.val)
                if index == 0: 
                    head = final_list.next
                list2 = list2.next
                final_list = final_list.next
            else: 
                final_list.next = ListNode(list1.val)
                if index == 0: 
                    head = final_list.next
                list1 = list1.next
                final_list = final_list.next
            index = index + 1
        
        while list1:
            final_list.next = ListNode(list1.val)
            if index == 0: 
                head = final_list.next
            list1 = list1.next
            final_list = final_list.next
            index = index + 1
        
        while list2:
            final_list.next = ListNode(list2.val)
            if index == 0: 
                head = final_list.next
            list2 = list2.next
            final_list = final_list.next
            index = index + 1

        return head
    
# Helper function to convert a Python list to a linked list
def to_linked_list(elements):
    if not elements:  # If the list is empty
        return None
    head = ListNode(elements[0])
    current = head
    for value in elements[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list to a Python list
def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test cases
# Test 1
# firstlist = [1, 2, 4]
# secondlist = [1, 3, 4]
# Test 2
#firstlist = []
#secondlist = []
# Test 3
#firstlist = [0]
#secondlist = []
# Test 4
#firstlist = [1]
#secondlist = []
# Test 5
firstlist = [-10,-6,-6,-6,-3,5]
secondlist = []

# Convert the Python lists to linked lists
list1 = to_linked_list(firstlist)
list2 = to_linked_list(secondlist)

# Instantiate the Solution and call mergeTwoLists
solution = Solution()
merged_head = solution.mergeTwoLists(list1, list2)

# Convert the result back to a Python list for easy verification
merged_list = to_list(merged_head)

# Print the result
print("Merged List:", merged_list)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        init = ListNode(0, head)
        pointer_one = init
        pointer_two = init
        
        for _ in range(n + 1):
            pointer_one = pointer_one.next

        while pointer_one:
            pointer_one = pointer_one.next
            pointer_two = pointer_two.next
        
        pointer_two.next = pointer_two.next.next
        
        return init.next
    

def build_linked_list(values):
    """Convert a Python list into a linked list."""
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    """Convert a linked list back into a Python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

s = Solution()

head_case1 = build_linked_list([1,2,3,4,5])
new_head = s.removeNthFromEnd(head_case1, 2)
print(linked_list_to_list(new_head))  # [1, 2, 3, 5]

head_case2 = build_linked_list([1])
new_head = s.removeNthFromEnd(head_case2, 1)
print(linked_list_to_list(new_head))  # []

head_case3 = build_linked_list([1, 2])
new_head = s.removeNthFromEnd(head_case3, 1)
print(linked_list_to_list(new_head))  # [1]
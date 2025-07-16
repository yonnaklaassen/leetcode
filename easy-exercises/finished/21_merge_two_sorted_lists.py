class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        current = dummy
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1 is not None:
                current.next = list1
        if list2 is not None:
                current.next = list2
        return dummy.next
    
s = Solution()

def print_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)

case1_list1 = ListNode(1, ListNode(2, ListNode(4)))
case1_list2 = ListNode(1, ListNode(3, ListNode(4)))
merged = s.mergeTwoLists(case1_list1, case1_list2)
print_list(merged)  # [1,1,2,3,4,4]

case2_list1 = None
case2_list2 = None
merged = s.mergeTwoLists(case2_list1, case2_list2)
print_list(merged)  # []

case3_list1 = None
case3_list2 = ListNode(0)
merged = s.mergeTwoLists(case3_list1, case3_list2)
print_list(merged)  # [0]

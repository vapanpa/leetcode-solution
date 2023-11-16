# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reversal(head, buildList):
            if head == None:
                return buildList
            else:
                newList = ListNode(val = head.val, next = buildList)
                return reversal(head.next, newList)
        return reversal(head, None)

# general notes:
# in python recursive calls need the 'return' keyword with it.

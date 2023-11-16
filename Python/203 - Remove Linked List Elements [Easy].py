# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None: 
            return head
        elif head.val == val:
            return self.removeElements(head.next, val)
        else:
            head.next = self.removeElements(head.next, val)
            return head


# this does not use helper functions. therefore, you must use `self` to utilize functions since there is no instance of `Solution`

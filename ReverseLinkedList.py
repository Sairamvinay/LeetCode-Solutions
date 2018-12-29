#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        L = []
        while (head):
            L.append(head.val)
            head = head.next
        
        L.reverse()
        head = ListNode(0)
        curr = head
        for val in L:
            curr.next = ListNode(val)
            curr = curr.next
        
        curr.next = None
        return head.next

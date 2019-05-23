from sets import Set
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        D = Set()
        curr = head
        while curr:
            if curr in D:
                return curr
            
            else:
                D.add(curr)
                curr = curr.next
        
        return None

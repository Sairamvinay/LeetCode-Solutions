class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        D = Set()
        i = 0
        while curr:
            if curr in D:
                return True
            
            else:
                D.add(curr)
                curr = curr.next
        
        return False

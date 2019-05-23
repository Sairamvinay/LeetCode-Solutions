class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        L = []
        curr = head
        while curr:
            
            if curr.val not in L:
                L.append(curr.val)
            
            curr = curr.next
         
        ans = ListNode(0)
        c = ans
        while L:
            c.next = ListNode(L.pop(0))
            c = c.next
        
        return ans.next

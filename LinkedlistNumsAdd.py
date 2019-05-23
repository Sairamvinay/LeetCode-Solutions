class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        L = ListNode(0)
        curr = L
        carry = 0
        while (l1 and l2):
            value = l1.val + l2.val + carry
            if value >= 10:
                value = value - 10
                carry = 1
            else:
                carry = 0
            l1 = l1.next
            l2 = l2.next
            curr.next = ListNode(value)
            curr = curr.next
        
        
       
        while l1:
            value = l1.val + carry
            if value >= 10:
                carry = 1
                value -= 10
            
            else:
                carry = 0
            
            curr.next = ListNode(value)
            curr = curr.next
            l1 = l1.next
        
        while l2:
            
            value = l2.val + carry
            if value >= 10:
                carry = 1
                value -= 10
            
            else:
                carry = 0
            
            curr.next = ListNode(value)
            curr = curr.next
            l2 = l2.next
            
        if (carry == 1):
            curr.next = ListNode(1)
            curr = curr.next
        
        else:
            pass
        
        
        
        return L.next
        

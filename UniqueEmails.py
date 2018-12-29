class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        
        # create hash of the formatted strings stored in dictionary with the counts
        D = {}
        for email in emails:
            names = email.split("@")
            local = names[0]
            domain = names[1]
            if local.find("+") != -1:
                local = local[:local.find("+"):]
            
            local = local.replace(".","")
            email = local + "@" + domain
            if email in D:
                D[email] += 1
            
            else:
                D[email] = 1
            
            
        
        return len(D)
    
    
            
        

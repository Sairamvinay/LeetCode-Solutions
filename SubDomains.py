class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        counts = {}
        for domain in cpdomains:
            
            count,address = domain.split(" ")
            count = int(count)
            c = address.count(".")
            if address not in counts:
                counts[address] = count
                if c == 1:
                    top = address[1+address.find(".")::]
                    if top not in counts:
                        counts[top] = count
                
                    else:
                        counts[top] += count
            
                else:
                    nxt = address[1+address.find(".")::]
                    low = nxt[1+nxt.find(".")::]
                    if nxt not in counts:
                        if low not in counts:
                            counts[nxt] = count
                            counts[low] = count
                    
                        else:
                            counts[nxt] = count
                            counts[low] += count
                
                    else:
                        if low not in counts:
                            counts[nxt] += count
                            counts[low] = count
                    
                        else:
                            counts[nxt] += count
                            counts[low] += count
            
            
            else:
                counts[address] += count
                if c == 1:
                    top = address[1+address.find(".")::]
                    if top not in counts:
                        counts[top] = count
                
                    else:
                        counts[top] += count
            
                else:
                    nxt = address[1+address.find(".")::]
                    low = nxt[1+nxt.find(".")::]
                    if nxt not in counts:
                        if low not in counts:
                            counts[nxt] = count
                            counts[low] = count
                    
                        else:
                            counts[nxt] = count
                            counts[low] += count
                
                    else:
                        if low not in counts:
                            counts[nxt] += count
                            counts[low] = count
                    
                        else:
                            counts[nxt] += count
                            counts[low] += count
            
            
        domains = []
        for key in counts:
            domains.append(str(counts[key]) + ' ' + key)
                
            
        return domains
                

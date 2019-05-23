def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        dim = len(nums) * len(nums[0])
        if r*c != dim:
            return nums
        
        
        else:
            reshape = []
            a = 0
            b = 0
            tmp = []
            for i in range(len(nums)):
                for j in range(len(nums[0])):
                    
                    if b == (c-1):
                        
                        tmp.append(nums[i][j])
                        reshape.append(tmp)
                        tmp = []
                        b = 0
                        a += 1
                    
                    else:
                        tmp.append(nums[i][j])
                        b += 1
                    
                    
                
            
            return reshape

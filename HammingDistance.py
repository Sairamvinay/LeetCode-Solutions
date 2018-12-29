class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        k = x ^ y
        X  = "{0:b}".format(k)
        return X.count("1")

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        res = str(x) == str(x)[::-1]
        return bool(res)
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        contador = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[contador] = nums[i]
                contador += 1
        
        return contador
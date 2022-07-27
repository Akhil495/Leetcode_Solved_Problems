class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, output = 0,0        
        for right, n in enumerate(nums):
            if n == 0:
                left = right + 1
            output = max(output, right-left+1)
        return output    

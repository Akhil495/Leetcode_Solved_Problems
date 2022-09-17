class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = False
        dec = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                dec = True   
            elif nums[i] < nums[i+ 1]:
                inc = True
                
            if inc==True and dec==True:
                return False

        return True       
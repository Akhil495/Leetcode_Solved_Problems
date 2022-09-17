class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        l = ""
        for i in num:
            l+=str(i)
        return [int(i) for i in str(int(l)+k)]    
            
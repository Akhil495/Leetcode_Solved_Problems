class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # return collections.Counter(nums).most_common(1)[0][0]
        hash_map = {}
        for i in nums:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                return i
            
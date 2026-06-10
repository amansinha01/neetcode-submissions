class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,j in enumerate(nums):
            n = target-j
            if n in d:
                return [d[n], i]
            d[j] = i 
        return []
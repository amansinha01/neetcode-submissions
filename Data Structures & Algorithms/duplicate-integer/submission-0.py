class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct_list = list(set(nums))
        if len(nums) == len(distinct_list):
            return False
        return True
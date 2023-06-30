class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = set()
        i = 0
        while i < len(nums):
            if nums[i] not in res:
                res.add(nums[i])
                i +=1
            else:
                nums.remove(nums[i])
        return len(res)
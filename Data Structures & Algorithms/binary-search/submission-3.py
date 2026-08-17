class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums)
        while a < b:
            c = (a + b) // 2
            if target == nums[c]:
                return c
            elif target < nums[c]:
                b = c
            elif target > nums[c]:
                a = c + 1
        return -1
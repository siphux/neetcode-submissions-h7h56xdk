class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)

        # ans = [nums[i] if i in range(len(nums)) else nums[i - len(nums)] for i in range(2 * len(nums))]
        return ans
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_length = 0
        for num in nums:
            if num - 1 not in s:
                current = num
                length = 1
                while current + 1 in s:
                    current += 1
                    length += 1
                if length > max_length:
                    max_length = length 
        print(s)
        return max_length
            
            

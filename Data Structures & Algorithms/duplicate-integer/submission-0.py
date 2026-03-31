class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for elem in nums:
            if elem not in dic:
                dic[elem] = 0
            if dic[elem] > 0:
                return True
            dic[elem]+=1
        return False

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
        return [key for (key, value) in sorted(dic.items(), reverse = True, key = lambda x: x[1])][:k]

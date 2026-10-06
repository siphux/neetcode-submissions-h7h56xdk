class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        from collections import Counter
        c_s = Counter(s)
        c_t = Counter(t)
        return c_s == c_t
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)-len(t) != 0:
            return False
        s = sorted(s)
        t = sorted(t)
        for l1, l2 in zip(s, t):
            if l1 != l2:
                return False
        return True
